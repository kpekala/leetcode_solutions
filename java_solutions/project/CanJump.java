import java.util.Arrays;

public class CanJump {

    public boolean canJump(int[] nums) {
        if (nums.length == 1)
            return true;
        boolean[] been = new boolean[nums.length];
        return canJumpRecursive(nums, 0, been);
    }

    private boolean canJumpRecursive(int[] nums, int index, boolean[] been) {
        if (been[index])
            return false;
        been[index] = true;
        if (index == nums.length - 1)
            return true;
        for (int i = 1; i <= nums[index]; i++) {
            int newPosition = index + i;
            if(newPosition < nums.length && canJumpRecursive(nums, newPosition, been)){
                return true;
            }
        }
        return false;
    }

    public void test(int[] nums) {
        System.out.println("Result for array " + Arrays.toString(nums) + " : " + canJump(nums));
    }
}
