import java.util.Scanner;

public class _1052_Rabbit_Hunt {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();

        int num;
        //int i,j,k;


        int x[] = new int[200];
        int y[] = new int[200];

        for (int i = 0; i < n; i++) {
            x[i] = input.nextInt();
            y[i] = input.nextInt();
        }
        int max = 0;

        for (int i = 0; i < n - 1; i++) {

            for (int j = i + 1; j < n - 1; j++) {
                num = 2;

                for (int k = j + 1; k < n; k++) {
                    if ((x[k] - x[i]) * (y[j] - y[i]) == (x[j] - x[i]) * (y[k] - y[i])) {
                        num++;
                        //System.out.println(num);
                    }


                }

                if (max < num) {
                    max = num;
                    //System.out.println(max);
                }
            }



        }

        System.out.println(max);


    }

}