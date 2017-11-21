import java.awt.geom.Point2D;
import java.util.Scanner;

public class _1020_Rope {
    public static void main(String [] args){
       try(Scanner input = new Scanner(System.in)){
           while(input.hasNext()){
               int n = input.nextInt();

               double r = input.nextDouble();

               Point2D.Double points[] = new Point2D.Double[n];

               for(int i = 0; i< n; i++){
                   points[i] = new Point2D.Double(input.nextDouble(),input.nextDouble());

               }
               double result = 2 * Math.PI * r;
               if(n > 1){
                   for (int i = 1; i<n; i++){
                       result += points[i].distance(points[i -1]);

                   }

                   result += points[n-1].distance(points[0]);
               }

               System.out.println(String.format("%.2f", result));
           }
       }

    }
}
