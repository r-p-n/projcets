package au.edu.jcu.measurementconverter;

import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
    @Test
    public void testUnitConversionBaseline() {
        Converter converter = new Converter();

        String mmToIn = converter.ConvertUnits("MM", "IN", 1f,
                6, "Metric to Imperial");
        String mmToFt = converter.ConvertUnits("MM", "FT", 1f,
                6, "Metric to Imperial");
        String mmToYd = converter.ConvertUnits("MM", "YD", 1f,
                6, "Metric to Imperial");
        String mmToMi = converter.ConvertUnits("MM", "MI", 1f,
                6, "Metric to Imperial");

        String cmToIn = converter.ConvertUnits("CM", "IN", 1f,
                6, "Metric to Imperial");
        String cmToFt = converter.ConvertUnits("CM", "FT", 1f,
                6, "Metric to Imperial");
        String cmToYd = converter.ConvertUnits("CM", "YD", 1f,
                6, "Metric to Imperial");
        String cmToMi = converter.ConvertUnits("CM", "MI", 1f,
                6, "Metric to Imperial");

        String mToIn = converter.ConvertUnits("M", "IN", 1f,
                6, "Metric to Imperial");
        String mToFt = converter.ConvertUnits("M", "FT", 1f,
                6, "Metric to Imperial");
        String mToYd = converter.ConvertUnits("M", "YD", 1f,
                6, "Metric to Imperial");
        String mToMi = converter.ConvertUnits("M", "MI", 1f,
                6, "Metric to Imperial");

        String kmToIn = converter.ConvertUnits("KM", "IN", 1f,
                6, "Metric to Imperial");
        String kmToFt = converter.ConvertUnits("KM", "FT", 1f,
                6, "Metric to Imperial");
        String kmToYd = converter.ConvertUnits("KM", "YD", 1f,
                6, "Metric to Imperial");
        String kmToMi = converter.ConvertUnits("KM", "MI", 1f,
                6, "Metric to Imperial");

        assertEquals(mmToIn, "0.0393701");
        assertEquals(mmToFt, "0.0032808");
        assertEquals(mmToYd, "0.0010936");
        assertEquals(mmToMi, "0.0000006");

        assertEquals(cmToIn, "0.3937008");
        assertEquals(cmToFt, "0.0328084");
        assertEquals(cmToYd, "0.0109361");
        assertEquals(cmToMi, "0.0000062");

        assertEquals(mToIn, "39.3700790");
        assertEquals(mToFt, "3.2808399");
        assertEquals(mToYd, "1.0936130");
        assertEquals(mToMi, "0.0006214");

        assertEquals(kmToIn,"39370.0781250");
        assertEquals(kmToFt,"3280.8398438");
        assertEquals(kmToYd,"1093.6130371");
        assertEquals(kmToMi,"0.6213712");
    }

    @Test
    public void testUnitConversionLowDecimal() {
        Converter converter = new Converter();

        String mmToIn = converter.ConvertUnits("MM", "IN", 1f,
                1, "Metric to Imperial");

        assertEquals(mmToIn, "0.04");
    }

    @Test
    public void testUnitConversionHighDecimal() {
        Converter converter = new Converter();

        String mmToIn = converter.ConvertUnits("MM", "IN", 1f,
                7, "Metric to Imperial");

        assertEquals(mmToIn, "0.03937008");
    }

    @Test
    public void testUnitConversionImperialToMetric() {
        Converter converter = new Converter();

        String inToMm = converter.ConvertUnits("MM", "IN", 1f,
                1, "Imperial to Metric");

        String ftToCm = converter.ConvertUnits("CM", "FT", 1f,
                1, "Imperial to Metric");

        String ydToM = converter.ConvertUnits("M", "YD", 1f,
                1, "Imperial to Metric");

        String miToKm = converter.ConvertUnits("KM", "MI", 1f,
                1, "Imperial to Metric");

        assertEquals(inToMm, "25.40");
        assertEquals(ftToCm, "30.48");
        assertEquals(ydToM, "0.91");
        assertEquals(miToKm, "1.61");
    }

    @Test
    public void testUnitConversionWithDecimal() {
        Converter converter = new Converter();

        String inToMm = converter.ConvertUnits("MM", "IN", 1.35f,
                2, "Imperial to Metric");

        assertEquals(inToMm, "34.290");
    }
}