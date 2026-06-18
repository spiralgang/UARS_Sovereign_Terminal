package com.spiralgang.uars.enforcer.launcher;

import android.app.Application;
import android.util.Log;

public class UARSApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        Log.i("UARS", "Sovereign AI Environment Initialized");
    }
}
