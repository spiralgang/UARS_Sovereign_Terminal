package com.spiralgang.uars.enforcer.launcher.ui;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import com.spiralgang.uars.enforcer.launcher.core.AIProfileManager;
import com.spiralgang.uars.enforcer.launcher.network.UARSEnforcementEngine;
import java.util.List;
import java.util.stream.Collectors;

public class LauncherActivity extends AppCompatActivity {
    private UARSEnforcementEngine enforcementEngine = new UARSEnforcementEngine();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(32, 32, 32, 32);
        layout.setBackgroundColor(0xFF000000);

        TextView title = new TextView(this);
        title.setText("UARS+ SOVEREIGN TERMINAL");
        title.setTextColor(0xFF00FF00);
        title.setTextSize(24);
        layout.addView(title);

        EditText commandInput = new EditText(this);
        commandInput.setTextColor(0xFFFFFFFF);
        commandInput.setHint("Enter BASH Command...");
        commandInput.setHintTextColor(0xFF888888);
        layout.addView(commandInput);

        Button executeBtn = new Button(this);
        executeBtn.setText("EXECUTE");
        layout.addView(executeBtn);

        TextView outputText = new TextView(this);
        outputText.setTextColor(0xFF00FF00);
        layout.addView(outputText);

        executeBtn.setOnClickListener(v -> {
            String cmd = commandInput.getText().toString();
            String result = enforcementEngine.executeCommand(cmd);
            outputText.setText(result);
        });

        setContentView(layout);
    }
}
