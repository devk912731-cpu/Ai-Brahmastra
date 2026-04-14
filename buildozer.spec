[app]
title = Brahmastra
package.name = brahmastra
package.domain = org.raj.panini
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pillow
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
