package com.spiralgang.uars.enforcer.launcher.core;

import android.app.admin.DevicePolicyManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class SovereignDeviceAdminReceiver extends DeviceAdminReceiver {
    @Override
    public void onEnabled(Context context, Intent intent) {
        DevicePolicyManager dpm = (DevicePolicyManager) context.getSystemService(Context.DEVICE_POLICY_SERVICE);
        ComponentName admin = new ComponentName(context, SovereignDeviceAdminReceiver.class);
        
        // Sovereign Policy: Aggressive Lockdown
        dpm.setCameraDisabled(admin, true);
        dpm.setPasswordQuality(admin, DevicePolicyManager.PASSWORD_QUALITY_COMPLEX);
        
        Toast.makeText(context, "Sovereign Administrator Enabled: Lockdown Active", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onDisabled(Context context, Intent intent) {
        Toast.makeText(context, "Sovereign Administrator Disabled: System Vulnerable", Toast.LENGTH_SHORT).show();
    }
}
