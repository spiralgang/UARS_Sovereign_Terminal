package com.spiralgang.uars.enforcer.launcher.ui;

import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.Context;
import android.widget.RemoteViews;
import com.spiralgang.uars.enforcer.launcher.R;
import com.spiralgang.uars.enforcer.launcher.core.AIProfileManager;

public class DashboardWidgetProvider extends AppWidgetProvider {
    @Override
    public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {
        for (int appWidgetId : appWidgetIds) {
            RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.uars_widget_layout);
            
            // Display System Identity on Widget
            String identity = AIProfileManager.getSystemIdentity();
            views.setTextViewText(R.id.widget_title, "UARS+ SOVEREIGN");
            views.setTextViewText(R.id.widget_content, identity.split("\n")[0]); // Show model only for space
            
            appWidgetManager.updateAppWidget(appWidgetId, views);
        }
    }
}
