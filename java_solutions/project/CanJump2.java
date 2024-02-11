import java.util.Arrays;

public class CanJump2 {
    public int jump(int[] nums) {
        if (nums.length == 1)
            return 0;
        boolean[] been = new boolean[nums.length];
        int[] finalSteps = new int[nums.length];
        return jumpRecursive(nums, 0, been, 0, finalSteps);
    }

    private int jumpRecursive(int[] nums, int index, boolean[] been, int steps, int[] finalSteps) {
        if (index == nums.length - 1){
            return steps;
        }
        if (been[index])
            return finalSteps[index] + steps;
        been[index] = true;

        int minJumps = nums.length;

        for (int i = 1; i <= nums[index]; i++) {
            int newPosition = index + i;
            if(newPosition < nums.length){
                minJumps = Math.min(minJumps, jumpRecursive(nums, newPosition, been, steps + 1, finalSteps));
            }
        }
        finalSteps[index] = minJumps - steps;
        return minJumps;
    }

    public void test(int[] nums) {
        System.out.println("Result for array " + Arrays.toString(nums) + " : " + jump(nums));
    }

    public static void test() {
        new CanJump2().test(new int[] {2,3,1,1,4});
        new CanJump2().test(new int[] {2,3,0,1,4});
        new CanJump2().test(new int[] {1,2,1,1,1});
    }
}
