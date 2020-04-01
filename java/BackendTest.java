import org.apache.commons.io.FileUtils;
import org.junit.Assert;

import java.io.*;


public class BackendTest {
    public static void main(String[] args) throws IOException {
        undo();
        testAdd();
        undo();
        testBuy();
        undo();
        testSell();
        undo();
        testCreate();
        undo();
        testDelete();
        undo();
        testRefund();
        undo();
        testModify();
        undo();
        testMerger();
        undo();
        testMain();
    }

    public static void testAdd() throws IOException {
        Updater update = new Updater();
        update.addC("06 username2       BS 001000.00");
        //statement coverage
        Assert.assertEquals(FileUtils.readLines(new File("java/output/add1_uaf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/uaf.txt"), "UTF-8"));

        //loop coverage

    }

    public static void testBuy() throws IOException {
        Updater update = new Updater();
        //statement coverage
        update.buy("04 Concert3             username3     094 300.00");
        Assert.assertEquals(FileUtils.readLines(new File("java/output/buy1_uaf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/uaf.txt"), "UTF-8"));

        Assert.assertEquals(FileUtils.readLines(new File("java/output/buy1_atf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/atf.txt"), "UTF-8"));
    }


    public static void testSell() throws IOException {
        Updater update = new Updater();
        update.sell("03 Little House 5      username1      009 015.00");
        Assert.assertEquals(FileUtils.readLines(new File("java/output/sell1_atf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/atf.txt"), "UTF-8"));
    }


    public static void testCreate() throws IOException {
        Updater update = new Updater();
        update.create("01 usertest321     BS 000500.00");
        Assert.assertEquals(FileUtils.readLines(new File("java/output/create1_uaf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/uaf.txt"), "UTF-8"));
    }

    public static void testDelete() throws IOException {
        Updater update = new Updater();
        update.delete("02 username1       FS 999000.00");
        Assert.assertEquals(FileUtils.readLines(new File("java/output/delete1_uaf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/uaf.txt"), "UTF-8"));

        Assert.assertEquals(FileUtils.readLines(new File("java/output/delete1_atf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/atf.txt"), "UTF-8"));
    }

    public static void testRefund() throws IOException {
        Updater update = new Updater();
        update.refund("05 username2      username3      000200.00");
        Assert.assertEquals(FileUtils.readLines(new File("java/output/refund1_uaf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/uaf.txt"), "UTF-8"));
    }

    public static void testModify() throws IOException {
        Updater update = new Updater();
        update.modifyFile("src/uaf.txt", "username2       BS 001000.00", "username2       BS 002000.00");
        Assert.assertEquals(FileUtils.readLines(new File("java/output/add1_uaf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/uaf.txt"), "UTF-8"));
    }

    public static void testMerger() throws IOException {
        Main main = new Main();
        main.merger();

        Assert.assertEquals(FileUtils.readLines(new File("java/output/merger1_dtf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("dtf.txt"), "UTF-8"));
    }

    public static void testMain() throws IOException {
        Main main = new Main();
        String[] args = null;
        final InputStream original = System.in;
        final FileInputStream fips = new FileInputStream(new File("java/Main.java"));
        System.setIn(fips);
        Main.main(args);
        System.setIn(original);

        Assert.assertEquals(FileUtils.readLines(new File("java/output/main1_dtf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("dtf.txt"), "UTF-8"));
        Assert.assertEquals(FileUtils.readLines(new File("java/output/main1_atf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/atf.txt"), "UTF-8"));
        Assert.assertEquals(FileUtils.readLines(new File("java/output/main1_uaf_EO.txt"), "UTF-8"),
                FileUtils.readLines(new File("src/uaf.txt"), "UTF-8"));

    }

    public static void undo() throws IOException {
        FileWriter fw = new FileWriter("src/uaf.txt");
        fw.write("username1       FS 999000.00\n");
        fw.write("username2       BS 001000.00\n");
        fw.write("username3       SS 000500.99\n");
        fw.write("username4       AA 500000.00\n");
        fw.write("admin1          AA 001500.00\n");
        fw.write("nomoney         FS 000000.00\n");
        fw.close();

        fw = new FileWriter("src/atf.txt");
        fw.write("Concert1            username4      030 050.00\n");
        fw.write("Concert2            username1      079 250.00\n");
        fw.write("Concert3            username3      100 300.00\n");
        fw.write("END");
        fw.close();

    }
}
