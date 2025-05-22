[app]
title = Android Evolutivo
package.name = androidevolutivo
package.domain = org.eduartoba
source.dir = .
version = 0.1
entrypoint = main.py
android.permissions = INTERNET
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.arch = armeabi-v7a
android.logcat = 1
android.debug = 1
android.sdk_path = $ANDROID_SDK_ROOT
android.python3 = True
