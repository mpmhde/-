import java.util.Map;

public class ExampleHashMap {
    public static void main(String[] args) {
        Map<String, Integer> data = Map.of("груша", 50, "клубника", 30, "вишня", 25);
        data.forEach((k, v) -> System.out.println(k + " -> " + v));
    }
}