package 입출력과사칙연산.Q18108;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int year = 0;
        try {
            year = Integer.parseInt(br.readLine());
            System.out.println((year - 544 + 1));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
