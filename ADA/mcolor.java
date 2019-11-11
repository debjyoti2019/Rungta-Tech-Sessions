import java.io.*;
import java.util.Arrays;
public class mcolor {
    void print(int[] selected, int N){
        System.out.print("[");
        for (int i = 0; i < N ; i++) {
            System.out.print(" "+selected[i]);

        }
        System.out.print(" ]  ");
    }

    boolean solve(int vertex, int[][]array,int[]selected,int N,int m){
        if (vertex==N) {
            print(selected, N);
            return true;
        }
        for (int i = 1; i <= m ; i++) {
            int j;
            for (j = 0; j <N ; j++) {
                if(array[vertex][j]==0) continue;
                else {
                    if (selected[j]==i) break;

                }

            }
            if(j==N){
                selected[vertex]=i;

                if(solve(++vertex,array,selected,N,m))

                    return true;
                return false;
            }

        }
        return false;
    }

    public static void main (String args[]) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int N;
        N= Integer.parseInt(br.readLine());
        int adj[][]=new int[N][N];

        int selected[]=new int[N];
        Arrays.fill(selected,0);
        for (int i = 0; i < N ; i++) {
            String[] input;
            input = br.readLine().split("\\s");
            for (int j = 0; j <N ; j++) adj[i][j] = Integer.parseInt(input[j]);
            }
        System.out.println("Enter m: ");
        int m= Integer.parseInt(br.readLine());
        mcolor obj=new mcolor();



        if(obj.solve(0,adj,selected,N,m)==true)
            System.out.println("YES");
        else
            System.out.println("NO");
        }
    }
