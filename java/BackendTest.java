import jdk.jfr.StackTrace;
import org.apache.commons.io.FileUtils;
import org.junit.Assert;
import org.junit.*;
import java.io.*;

import static org.junit.Assert.*;

public class BackendTest {
    public void testAdd() throws IOException {
        Updater update = new Updater();
        File dir = new File("/output/");
        File[] dirList = dir.listFiles();
        if (dirList != null){
            for (File output : dirList){
                //update.addC();
                File input = new File("/input/"+ output.getName());
                Assert.assertEquals(FileUtils.readLines(input), FileUtils.readLines(output));

            }
        }
        //Input file to be tested in the updater method

        //this compares maybe im just doing alot of googling


    }
}
