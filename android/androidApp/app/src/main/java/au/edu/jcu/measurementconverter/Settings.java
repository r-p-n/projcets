package au.edu.jcu.measurementconverter;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.SeekBar;

public class Settings extends AppCompatActivity {
    final static int SETTINGS_REQUEST = 0;
    RadioGroup conversionType;
    SeekBar decimalPrecision;

    RadioButton selectedType;
    int precision;
    // conversion order is weather it's metric to imperial or imperial to metric
    boolean conversionOrderSwapped;

    // need initial to see if it was changed or not
    int initialConversionTypeSelectedId;
    int conversionTypeSelectedId;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);
        getWidgets();
        getSavedSettings();
        getInitialConversionTypeSelectedId();
    }

    public void backOnClick(View view) {
        getConversionTypeSelectedId();
        getWidgets();

        setIntentValues();
        createIntent(selectedType, precision, conversionOrderSwapped);
        saveSettings();
    }

    private void createIntent(RadioButton selectedType, int precision,
                              boolean conversionOrderSwapped) {
        Intent intent = new Intent();
        intent.putExtra("selectedType", selectedType.getText());
        intent.putExtra("precision", precision);
        intent.putExtra("swapped", conversionOrderSwapped);
        setResult(RESULT_OK, intent);
        finish();
    }

    private void saveSettings() {
        SharedPreferences settings = getSharedPreferences("Settings", 0);
        SharedPreferences.Editor editor = settings.edit();
        editor.putInt("precision", precision);
        editor.putInt("ID", conversionTypeSelectedId);
        editor.apply();
    }

    private void getSavedSettings() {
        SharedPreferences settings = getSharedPreferences("Settings", 0);
        decimalPrecision.setProgress(settings.getInt("precision", 0));
        conversionType.check(settings.getInt("ID", conversionType.getCheckedRadioButtonId()));
    }

    private void setIntentValues() {
        selectedType = findViewById(conversionTypeSelectedId);
        precision = decimalPrecision.getProgress();
        conversionOrderSwapped = !(initialConversionTypeSelectedId ==
                                    conversionType.getCheckedRadioButtonId());
    }

    private void getWidgets() {
        decimalPrecision = findViewById(R.id.precision);
        conversionType = findViewById(R.id.conversionType);
    }

    private void getConversionTypeSelectedId() {
        conversionTypeSelectedId = conversionType.getCheckedRadioButtonId();
    }

    private void getInitialConversionTypeSelectedId() {
        initialConversionTypeSelectedId = conversionType.getCheckedRadioButtonId();
    }
}
