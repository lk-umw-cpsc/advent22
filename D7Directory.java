import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.HashMap;
import java.util.Map;

public class D7Directory {

    private final D7Directory parent;
    private final Map<String, D7Directory> subdirectories;
    private int contains;

    public D7Directory(D7Directory parent) {
        subdirectories = new HashMap<>();
        if (parent == null) {
            this.parent = this;
        } else {
            this.parent = parent;
        }
        contains = 0;
    }

    public D7Directory getSubdirectory(String name) {
        if (name.charAt(0) == '.') {
            return parent;
        }
        return subdirectories.get(name);
    }

    public void addSubdirectory(String name, D7Directory subdirectory) {
        subdirectories.put(name, subdirectory);
    }
    
    public void incrementFileSize(int byAmount) {
        contains += byAmount;
        if (parent != null && parent != this) {
            parent.incrementFileSize(byAmount);
        }
    }

    private static int p1sum = 0;
    private static int p2 = Integer.MAX_VALUE;
    private static int p2goal;

    public static void recursiveSearch(D7Directory directory) {
        int contains = directory.contains;
        if (contains <= 100000) {
            p1sum += contains;
        }
        for (D7Directory dir : directory.subdirectories.values()) {
            recursiveSearch(dir);
        }
        if (contains < p2 && contains >= p2goal) {
            p2 = contains;
        }
    }

    public static void main(String[] args) throws IOException {
        File f = new File("7.txt");
        // Read entire file into RAM
        String input = Files.readString(f.toPath());
        D7Directory root = new D7Directory(null);
        D7Directory cur = root;
        for (String line : input.split("\n")) {
            if (line.charAt(0) == '$') {
                String[] tokens = line.substring(2).split(" ");
                if (tokens[0].equals("cd")) {
                    String directory = tokens[1];
                    if (directory.equals("/")) {
                        cur = root;
                    } else {
                        cur = cur.getSubdirectory(directory);
                    }
                }
            } else {
                String[] tokens = line.split(" ");
                if (tokens[0].matches("\\d+")) {
                    int amount = Integer.parseInt(tokens[0]);
                    cur.incrementFileSize(amount);
                } else {
                    D7Directory newDir = new D7Directory(cur);
                    cur.addSubdirectory(tokens[1], newDir);
                }
            }
        }
        p2goal = 30000000 - (70000000 - root.contains);
        recursiveSearch(root);
        System.out.println("Part 1: " + p1sum);
        System.out.println("Part 2: " + p2);
    }
}