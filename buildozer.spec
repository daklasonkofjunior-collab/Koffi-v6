[app]
title = KOFFI V6
package.name = koffiv6
package.domain = com.koffi.v6
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreements = True
android.archs = armeabi-v7a, arm64-v8a
p4a.branch = master
android.permissions = INTERNET
