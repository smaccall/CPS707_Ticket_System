import jdk.jfr.StackTrace;
import org.junit.Test;
import static org.junit.Assert.*;

public class BackendTest {
    public void testAdd(){
        //Updater update = new Updater();

        //Input and output files i think should go here
        final File expected = new File();
        final File output =  File();
        //Input file to be tested in the updater method

        //this compares maybe im just doing alot of googling
        Assert.assertEquals(FileUtils.readlines(expected), FileUtils.readlines(output));

    }
}
