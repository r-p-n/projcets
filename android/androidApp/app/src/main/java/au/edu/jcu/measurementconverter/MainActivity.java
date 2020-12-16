package au.edu.jcu.measurementconverter;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    final static String METRIC_TO_IMPERIAL = "Metric to Imperial";
    final static String IMPERIAL_TO_METRIC = "Imperial to Metric";

    private Converter converter;

    Spinner imperialUnitContainer;
    Spinner metricUnitContainer;
    EditText userInputContainer;
    TextView resultText;

    String imperialUnitChoice;
    String metricUnitChoice;
    String result;
    String typeOrder;

    int unitIndex1;
    int unitIndex2;
    int decimalPrecision;

    Boolean conversionOrderSwapped = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getWidgets();
        getSavedSettings();
        converter = new Converter();
        if (savedInstanceState != null) {
            getSaveInstanceStateParams(savedInstanceState);
            setResultText();
        }
    }

    @Override
    public void onSaveInstanceState(@NonNull Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putLong("metricChoice", metricUnitContainer.getSelectedItemId());
        outState.putLong("imperialChoice", imperialUnitContainer.getSelectedItemId());
        outState.putString("result", result);
        // typeOrder is metric to imperial or imperial to metric
        outState.putString("typeOrder", typeOrder);
        // unitIndex are the index of the spinners (mm, cm, etc.)
        outState.putInt("unitIndex1", unitIndex1);
        outState.putInt("unitIndex2", unitIndex2);
        outState.putInt("decimalPrecision", decimalPrecision);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == Settings.SETTINGS_REQUEST) {
            if (resultCode == RESULT_OK) {
                if (data != null) {
                    decimalPrecision = data.getIntExtra("precision", 7);
                    typeOrder = data.getStringExtra("selectedType");
                    // is true if conversion order is changed in settings
                    conversionOrderSwapped = data.getBooleanExtra("swapped", false);
                }
            }
            setSavedSettings();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        unitIndex1 = imperialUnitContainer.getSelectedItemPosition();
        unitIndex2 = metricUnitContainer.getSelectedItemPosition();
    }

    @Override
    protected void onResume() {
        super.onResume();
        // spinner order refers to what spinner is placed before the other
        setSpinnerOrder();
        setSpinnerIndex();
    }

    public void converterOnClick(View view) {
        try {
            getWidgets();
            getResultText();
        } catch (NumberFormatException e) {
            //raised if no input is given
            result = "0";
        }
        setResultText();
    }

    public void settingsOnClick(View view) {
        Intent intent = new Intent(MainActivity.this, Settings.class);
        startActivityForResult(intent, Settings.SETTINGS_REQUEST);
    }

    private void getSaveInstanceStateParams(Bundle savedInstanceState) {
        metricUnitContainer.setSelection(savedInstanceState.getInt("metricChoice"));
        imperialUnitContainer.setSelection(savedInstanceState.getInt("imperialChoice"));
        result = savedInstanceState.getString("result");
        typeOrder = savedInstanceState.getString("typeOrder");
        decimalPrecision = savedInstanceState.getInt("decimalPrecision");
        unitIndex1 = savedInstanceState.getInt("unitIndex1");
        unitIndex2 = savedInstanceState.getInt("unitIndex2");
    }

    private void getWidgets() {
        imperialUnitContainer = findViewById(R.id.imperial);
        metricUnitContainer = findViewById(R.id.metric);
        userInputContainer = findViewById(R.id.input);
        resultText = findViewById(R.id.output);
    }

    private float getUserInput() {
        imperialUnitChoice = String.valueOf(imperialUnitContainer.getSelectedItem());
        metricUnitChoice = String.valueOf(metricUnitContainer.getSelectedItem());
        String userInputString = String.valueOf(userInputContainer.getText());
        return Float.parseFloat(userInputString);
    }

    private void setSpinnerIndex() {
        // if else because the spinners' position can be swapped
        if(conversionOrderSwapped){
            imperialUnitContainer.setSelection(unitIndex2);
            metricUnitContainer.setSelection(unitIndex1);
        }else
        {
            imperialUnitContainer.setSelection(unitIndex1);
            metricUnitContainer.setSelection(unitIndex2);
        }
    }

    private void setSpinnerOrder() {
        switch (typeOrder) {
            case (IMPERIAL_TO_METRIC):
                setSpinnerAdapters(R.array.spinner_imperial, R.array.spinner_metric);
                break;
            case (METRIC_TO_IMPERIAL):
                setSpinnerAdapters(R.array.spinner_metric, R.array.spinner_imperial);
                break;
        }
    }

    private ArrayAdapter<CharSequence> getSpinnerAdapter(int spinner) {
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, spinner,
                android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        return adapter;
    }

    private void setSpinnerAdapters(int spinner1, int spinner2) {
        metricUnitContainer.setAdapter(getSpinnerAdapter(spinner1));
        imperialUnitContainer.setAdapter(getSpinnerAdapter(spinner2));
    }

    private void getSavedSettings() {
        SharedPreferences settings = getSharedPreferences("Settings", 0);
        typeOrder = settings.getString("typeOrder", "Metric to Imperial");
        decimalPrecision = settings.getInt("decimalPrecision", 2);
    }

    private void setSavedSettings() {
        SharedPreferences settings = getSharedPreferences("Settings", 0);
        SharedPreferences.Editor editor = settings.edit();
        editor.putString("typeOrder", typeOrder);
        editor.putInt("decimalPrecision", decimalPrecision);
        editor.apply();
    }

    private void getResultText() {
        float userInput = getUserInput();
        result = converter.ConvertUnits(metricUnitChoice, imperialUnitChoice,
                userInput, decimalPrecision, typeOrder);
    }

    private void setResultText() {
        resultText.setText(result);
    }
}
