import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;

public class Day5 {

    public static void main(String[] args) {
        final Stack<Character>[] stacks = new Stack[10];
        final Stack<Character>[] stacksp2 = new Stack[10];
        for (int i = 1; i < 10; i++) {
            stacks[i] = new Stack<>();
            stacksp2[i] = new Stack<>();
        }
        try (Scanner in = new Scanner(new File("5.txt"), "UTF-8")) {
            String[] startingStackInput = new String[8];
            for (int i = 0; i < 8; i++) {
                startingStackInput[i] = in.nextLine();
            }
            for (int i = 7; i >= 0; i--) {
                for (int stack = 1; stack < 10; stack++) {
                    char c = startingStackInput[i].charAt(-3 + 4 * stack);
                    if (c != ' ') {
                        stacks[stack].push(c);
                        stacksp2[stack].push(c);
                    }
                }
            }
            in.nextLine(); in.nextLine();
            Stack<Character> lifted = new Stack<>();
            while (in.hasNextLine()) {
                String line = in.nextLine();
                String[] words = line.split(" ");
                int amount = Integer.parseInt(words[1]);
                int from = Integer.parseInt(words[3]);
                int to = Integer.parseInt(words[5]);

                for (int i = 0; i < amount; i++) {
                    char c = stacks[from].pop();
                    stacks[to].push(c);
                    lifted.push(stacksp2[from].pop());
                }
                for (int i = 0; i < amount; i++) {
                    stacksp2[to].push(lifted.pop());
                }
            }
            System.out.print("Part 1: ");
            for (int i = 1; i < 10; i++) {
                System.out.print(stacks[i].peek());
            }
            System.out.println();
            System.out.print("Part 2: ");
            for (int i = 1; i < 10; i++) {
                System.out.print(stacksp2[i].peek());
            }
            System.out.println();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

}