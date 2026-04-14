[app]
title = Brahmastra
package.name = brahmastra
package.domain = org.raj.panini
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyjnius==1.4.5,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE
