# Last Updated: 7 Jul 2024
# Creator: John Reed

from abc import ABC, abstractmethod
import platform

class Notification:
    """Notification represents a desktop notification
        Icon: str - A path to the image to use for the notification icon
        Summary: str - A short summary of the notification's contents (header)
        Body: str - The notification's full contents
    """

    def __init__(self) -> None:
        # Now, it may be the case that empty strings can mess things up, so I might have to fix that
        self._icon = ""
        self._summary = ""
        self._body = ""

    @property
    def Icon(self) -> str:
        return self._icon
    @Icon.setter
    def Icon(self, iconPath: str) -> None:
        self._icon = iconPath

    @property
    def Summary(self) -> str:
        return self._summary
    @Summary.setter
    def Summary(self, summary: str) -> None:
        self._summary = summary

    @property
    def Body(self) -> str:
        return self._body
    @Body.setter 
    def Body(self, body: str) -> None:
        self._body = body


class INotifier(ABC): 
    """`INotifier` exposes functions for showing `Notification`s on the desktop"""

    @abstractmethod
    def __init__(self, appName: str) -> None:
        """Start the notifier with a specified appName"""
        raise NotImplementedError()

    @abstractmethod
    def Show(self, notification: Notification):
        """`Show` takes a `Notification` and displays it"""
        raise NotImplementedError()


# This section is a mess but just imports the correct module for the system 
# (I had to do this because NixOS does not provide windows_toasts so I cannot import them, lol) - John Reed
if platform.system() == "Windows" and platform.release() in ["10", "11"]:
    from windows_toasts import Toast, ToastDisplayImage, WindowsToaster
    class WindowsNotifier(INotifier):
        def __init__(self, appName: str) -> None:
            self._toaster = WindowsToaster(appName)

        def Show(self, notification: Notification) -> None:
            # create windows_toasts toast from notification
            toastNotif = Toast()
            toastNotif.AddImage(ToastDisplayImage.fromPath(notification.Icon))
            toastNotif.text_fields = [
                notification.Summary,
                notification.Body
            ]

            # display toast
            self._toaster.show_toast(toastNotif)

elif platform.system() == "Linux":
    import dbus
    class DbusNotifier(INotifier):
        def __init__(self, appName: str) -> None:
            self._appName = appName

            item = "org.freedesktop.Notifications"

            self._notifyIntf = dbus.Interface(
                dbus.SessionBus().get_object(item, "/"+item.replace('.', '/')),
                item
            )

        def Show(self, notification: Notification) -> None:
            self._notifyIntf.Notify(
                self._appName,
                0, # replaces_id (which notification to replace, 0 means none)
                notification.Icon,
                notification.Summary,
                notification.Body,
                [], # list of actions (interactivity)
                {}, # hints (custom_audio, urgency level, etc)
                -1 # expire timout (-1 => notif server decides, 0 => never expire)
            )

else:
    raise ImportError("module doesn't support this system")

def GetNotifier(appName: str) -> INotifier:
    """`GetNotifier` gets the appropriate implementation of `INotifier` for the system"""
    if platform.system() == "Windows" and platform.release() in ["10", "11"]:
        return WindowsNotifier(appName)
    elif platform.system() == "Linux":
        return DbusNotifier(appName)
    else: 
        print("Your system is not yet supported, try Linux or Windows 10/11 instead. Sorry!")
        exit()

