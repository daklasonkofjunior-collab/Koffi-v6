[app]
title = KOFFI V6
package.name = koffiv6
package.domain = com.koffi.v6
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build-tools = 33.0.2
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a
p4a.branch = master
android.permissions = INTERNET
