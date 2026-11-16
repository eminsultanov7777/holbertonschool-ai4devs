public class bug3_fixed {
    // Return the arithmetic mean of an array of integers.
    public static double average(int[] values) {
        if (values == null || values.length == 0) {
            throw new IllegalArgumentException("Values cannot be empty");
        }

        long sum = 0;
        for (int value : values) {
            sum += value;
        }

        return (double) sum / values.length;
    }

    public static void main(String[] args) {
        int[] scores = {80, 81};
        System.out.println(average(scores));
    }
}
