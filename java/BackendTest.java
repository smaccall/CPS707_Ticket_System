import jdk.jfr.StackTrace;
import org.apache.commons.io.FileUtils;
import org.junit.Assert;
import org.junit.*;
import java.io.*;

import static org.junit.Assert.*;

public class BackendTest {
    public void testAdd() throws IOException {
        Main main = new Main();
        File dir = new File("/output/");
        File[] dirList = dir.listFiles();
        Updater update = new Updater();
        update.addC("06 username2       BS 001000.00");

        //statement coverage
        Assert.assertEquals(FileUtils.readLines(new File("add1_uad_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("placehold2.txt"), "UTF-8"));
    }

    public void testBuy(){

    }

    public void testBuy(){

    }

    public void testBuy(){

    }
}
