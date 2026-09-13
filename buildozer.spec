[app]
title = Koffi V6
package.name = koffiv6
package.domain = org.koffi.v6

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.6
requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.accept_sdk_license_agreement = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master
