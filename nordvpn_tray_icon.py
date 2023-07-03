import os
import subprocess
import wx
import wx.adv

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):

    def __init__(self,frame):
        wx.adv.TaskBarIcon.__init__(self)
        self.nordvpn_tray_icon_frame = frame

        self.application_folder = os.path.dirname(os.path.abspath(__file__))
        self.protected_icon = wx.Icon(os.path.join(self.application_folder, 'protected.png'), wx.BITMAP_TYPE_PNG)
        self.exposed_icon = wx.Icon(os.path.join(self.application_folder, 'exposed.png'), wx.BITMAP_TYPE_PNG)
        self.timer = wx.Timer(self)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
        self.update_icon(None)
        result = subprocess.run(['nordvpn', 'set', 'killswitch', 'True'], stdout=subprocess.PIPE).returncode
        print (f'KillSwitch Result: {result}')
        
        # Create a callback to update the icon every 1 second
        self.Bind(wx.EVT_TIMER, self.update_icon, self.timer)
        self.timer.Start(1000)


    def update_icon(self, event):
        # Execute a command to check the VPN status
        # If the VPN is connected, set the icon to protected
        # If the VPN is not connected, set the icon to exposed
        # exectute nordvpn status is terminal to get the status

        status_text = subprocess.run(['nordvpn', 'status'], stdout=subprocess.PIPE).stdout.decode().strip().removeprefix('-\r  \r\r-\r  \r')
        if "Status: Connected" in status_text:
            self.SetIcon(self.protected_icon, tooltip=status_text)
            self.protected_icon
            self.connection_status = True
        else:
            self.SetIcon(self.exposed_icon, tooltip=status_text)
            self.connection_status = False
        self.last_status = status_text


    def CreatePopupMenu(self):
        menu = wx.Menu()
        
        connect_menu_item:wx.MenuItem = create_menu_item(menu, 'Connect', self.on_connect_clicked)
        disconnect_menu_item:wx.MenuItem = create_menu_item(menu, 'Disconnect', self.on_disconnect_clicked)
        
        menu.AppendSeparator()
        
        create_menu_item(menu, 'Quit', self.on_quit_clicked)

        if self.connection_status == True:
            connect_menu_item.Enable(False)
            disconnect_menu_item.Enable(True)
        else:
            connect_menu_item.Enable(True)
            disconnect_menu_item.Enable(False)
        return menu
    
    def create_status_popup(self, message):
        menu = wx.Menu()
        status_menu_item:wx.MenuItem = create_menu_item(menu, message, self.do_nothing )
        return menu

    def on_left_down(self, event):
        self.PopupMenu(self.create_status_popup(self.last_status))

    def on_connect_clicked(self, event):
        result = subprocess.run(['nordvpn', 'set', 'killswitch', 'True'], stdout=subprocess.PIPE).returncode
        print (f'KillSwitch Result: {result}')
        result = subprocess.run(['nordvpn', 'c'], stdout=subprocess.PIPE).returncode
        print (f'Connection Result: {result}')

    def on_disconnect_clicked(self, event):
        result = subprocess.run(['nordvpn', 'set', 'killswitch', 'False'], stdout=subprocess.PIPE).returncode
        print (f'KillSwitch Result: {result}')
        result = subprocess.run(['nordvpn', 'd'], stdout=subprocess.PIPE).returncode
        print (f'Disconnection Result: {result}')

    def on_quit_clicked(self, event):
        result = subprocess.run(['nordvpn', 'set', 'killswitch', 'False'], stdout=subprocess.PIPE).returncode
        print (f'KillSwitch Result: {result}')
        result = subprocess.run(['nordvpn', 'd'], stdout=subprocess.PIPE).returncode
        print (f'Quit Result: {result}')
        self.nordvpn_tray_icon_frame.Close()

    def do_nothing(self, event):
        pass

class nordvpn_tray_icon_frame(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(1,1))
        panel = wx.Panel(self)
        self.nord_vpn_tray_icon = TaskBarIcon(self)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    #----------------------------------------------------------------------
    def onClose(self, evt):
        """
        Destroy the taskbar icon and the frame
        """
        self.nord_vpn_tray_icon.RemoveIcon()
        self.nord_vpn_tray_icon.Destroy()
        self.Destroy()

if __name__ == "__main__":
    nordvpn_tray_icon_application = wx.App()
    nordvpn_tray_icon_frame()
    nordvpn_tray_icon_application.MainLoop()