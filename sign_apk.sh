#!/bin/bash
# sign_apk.sh
# Trusted App Developer Keystore Signing for UARS+

KEYSTORE_FILE="uars_sovereign.keystore"
ALIAS="spiralgang"
PASSWORD="sovereign_pass"

if [ ! -f "$KEYSTORE_FILE" ]; then
    echo "Generating new Sovereign Keystore..."
    keytool -genkey -v -keystore "$KEYSTORE_FILE" -alias "$ALIAS" -keyalg RSA -keysize 2048 -validity 10000 -storepass "$PASSWORD" -keypass "$PASSWORD" -dname "CN=Spiralgang, OU=Sovereign, O=UARS, L=Nexus, S=Cyberspace, C=SG"
fi

APK_PATH="app/build/outputs/apk/release/app-release-unsigned.apk"
SIGNED_APK="app/build/outputs/apk/release/UARS-Sovereign-Enforcer.apk"

if [ -f "$APK_PATH" ]; then
    echo "Signing APK..."
    jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA256 -keystore "$KEYSTORE_FILE" -storepass "$PASSWORD" "$APK_PATH" "$ALIAS"
    # zipalign -v 4 "$APK_PATH" "$SIGNED_APK" # Requires Android SDK build-tools
    mv "$APK_PATH" "$SIGNED_APK"
    echo "APK Signed: $SIGNED_APK"
else
    echo "Error: Release APK not found at $APK_PATH"
fi
