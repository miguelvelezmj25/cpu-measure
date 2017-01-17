public class Measure {

    public static void main(String[] args) throws InterruptedException {
        int sleep = 0;
        int max = 10000000;

        if(args.length > 0) {
            sleep = Integer.parseInt(args[0]);
        }

        if(args.length > 1) {
            max = Integer.parseInt(args[1]);
        }

        System.out.println(sleep);

        for (int i = 1; i<max; i++) {
            boolean isPrimeNumber = true;

            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrimeNumber = false;
                    break; // exit the inner for loop
                }
            }

            if (isPrimeNumber) {
                System.out.println(i + " ");
                Thread.sleep(sleep);
            }
        }
    }

}
