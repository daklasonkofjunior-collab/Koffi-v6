[app]
title = BARA FACE
package.name = baraface
package.domain = com.bouake.baraface
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools_version = 34.0.0
android.ndk = 25b
android.accept_sdk_license_agreements = True
