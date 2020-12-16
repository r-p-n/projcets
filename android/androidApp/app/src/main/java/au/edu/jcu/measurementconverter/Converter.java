package au.edu.jcu.measurementconverter;

import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.Map;

class Converter {
    private Map<String, Float> units;

    Converter(){
        MakeUnitHashMap();
    }

    // conversionOrder is weather it's metric to imperial or imperial to metric
    String ConvertUnits(String metricUnit, String imperialUnit,
                        float input, int numberOfDecimalPlaces, String conversionOrder) {
        // decimalFormat gives the result the correct number of decimal places
        DecimalFormat decimalFormat = getDecimalFormat(numberOfDecimalPlaces);
        return getResult(metricUnit, imperialUnit, input, conversionOrder, decimalFormat);
    }

    private String getResult(String metricUnit, String imperialUnit, float input,
                             String conversionOrder, DecimalFormat decimalFormat) {
        // tried to get rid of warning with a map with a default return. Required higher min API
        float metricRatio = units.get(metricUnit);
        float imperialRatio = units.get(imperialUnit);

        switch (conversionOrder) {
            case ("Metric to Imperial"):
                return decimalFormat.format(metricRatio * imperialRatio * input);
            case ("Imperial to Metric"):
                return decimalFormat.format(input / imperialRatio / metricRatio);
        }
        // return null to stop a warning from popping up. Should never be reached.
        return null;
    }

    private DecimalFormat getDecimalFormat(int numberOfDecimalPlaces) {
        // gets the right decimal format (number of decimal places)
        StringBuilder decimalPrecision = getDecimalPrecision(numberOfDecimalPlaces);
        return new DecimalFormat(decimalPrecision.toString());
    }

    private StringBuilder getDecimalPrecision(int numberOfDecimalPlaces) {
        StringBuilder decimalPrecision = new StringBuilder("0.");
        // +1 to avoid 0 decimal places
        for (int i = 0; i < numberOfDecimalPlaces + 1; i++){
            decimalPrecision.append("0");
        }
        return decimalPrecision;
    }

    private void MakeUnitHashMap(){
        // using two of the values with a user input value gives the correct result
        // example: M -> IN = M * IN * value,  IN -> M = value / IN / M
        units = new HashMap<>();
        units.put("MM", 0.001f);
        units.put("CM", 0.01f);
        units.put("M", 1f);
        units.put("KM", 1000f);

        units.put("IN", 39.37008f);
        units.put("FT", 3.28084f);
        units.put("YD", 1.093613f);
        units.put("MI", 0.0006213712f);
    }
}
