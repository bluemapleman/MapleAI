本博客是个人原创的针对leetcode上的problem的解法，所有solution都基本通过了leetcode的官方Judging，个别未通过的例外情况会在相应部分作特别说明。


欢迎互相交流！

email: tomqianmaple@gmail.com

[toc]

# Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

- My Answer
```
package easy1;

import java.util.HashMap;
import java.util.Map;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class ContainsDuplicateII
{
    public static void main(String[] args)
    {
        int[] nums= {1,2,3,4,2,5,1,5,31};
        System.out.println(containsNearbyDuplicate(nums, 1));
    }
    
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        // A map that stores <Number, LastAppearIndex>.
        Map<Integer, Integer> map=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++) {
            int key=nums[i];
            if(map.containsKey(key)) {
                if(i-map.get(key)<=k)
                    return true;
            }
            map.put(key, i);
        }
        return false;
    }
}
```

# Implement Stack using Queues

Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

Notes:

- You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.

- Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.

- You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

- My Answer
```
package easy2;

import java.util.ArrayDeque;
import java.util.Queue;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
public class ImplementStackusingQueues
{
    Queue<Integer> queue1,queue2;
    public static void main(String[] args)
    {
        ImplementStackusingQueues queue=new ImplementStackusingQueues();
        queue.push(3);
        queue.push(2);
        queue.push(1);
        System.out.println(queue.top());
        System.out.println(queue.pop());
        System.out.println(queue.top());
        System.out.println(queue.empty());
        System.out.println(queue.pop());
        System.out.println(queue.pop());
        System.out.println(queue.empty());
    }
    
     /** Initialize your data structure here. */
    public ImplementStackusingQueues()
    {
        queue1=new ArrayDeque<Integer>();
        queue2=new ArrayDeque<Integer>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        queue1.add(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
            int ele=0;
        while(!queue1.isEmpty()) {
                if(queue1.size()==1) {
                    ele=queue1.peek();
                    queue1.poll();
                }
                else
                    queue2.add(queue1.poll());
        }
        while(!queue2.isEmpty())
                queue1.add(queue2.poll());
        return ele;
    }
    
    /** Get the top element. */
    public int top() {
        int ele=0;
        while(!queue1.isEmpty()) {
                if(queue1.size()==1) {
                    ele=queue1.peek();
                }
                queue2.add(queue1.poll());
        }
        while(!queue2.isEmpty())
                queue1.add(queue2.poll());
        return ele;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        if(queue1.size()==0)
                return true;
        else
                return false;
    }
    
}

```

# Invert Binary Tree

Invert a binary tree.
```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```
to
```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```
Trivia:

This problem was inspired by this original tweet by Max Howell:
> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class InvertBinaryTree
{
    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(4);
        TreeNode left1=new TreeNode(2),left2=new TreeNode(1),left3=new TreeNode(3);
        root.left=left1;left1.left=left2;left1.right=left3;
        TreeNode right1=new TreeNode(7),right2=new TreeNode(6),right3=new TreeNode(9);
        root.right=right1;right1.left=right2;right1.right=right3;
        TreeNode node=invertTree(root);
        System.out.println(node.left.left.val);
        System.out.println(node.right.val);
        System.out.println(node.right.left.val);
    }
    
    public static TreeNode invertTree(TreeNode root) {
        if(root==null)
            return null;
        TreeNode temp=root.left;
        root.left=root.right;
        root.right=temp;
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
        
    }
}

class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode(int x) { val = x; }
}
```

# Power of Two

Given an integer, write a function to determine if it is a power of two.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class PowerofTwo
{
    public static void main(String[] args)
    {
        System.out.println(isPowerOfTwo(8));
    }
    
    public static boolean isPowerOfTwo(int n) {
        // Any power of 2 can be divided by 2 to 1 finally.
        if(n==1)
            return true;
        while(n/2!=0 && n%2==0) {
                return isPowerOfTwo(n/2);
        }
        return false;
    }
}
```

# Implement Queue using Stacks

Implement the following operations of a queue using stacks.

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

Notes:

- You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.

- Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.

- You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

- My Answer
```
package easy2;

import java.util.Stack;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class ImplementQueueusingStacks
{
    Stack<Integer> stack1,stack2;
    
    public static void main(String[] args)
    {
        ImplementQueueusingStacks queue=new ImplementQueueusingStacks();
        queue.push(1);
        queue.push(2);
        queue.push(3);
        System.out.println(queue.pop());
        System.out.println(queue.empty());
        System.out.println(queue.peek());
        System.out.println(queue.pop());
        System.out.println(queue.pop());
        System.out.println(queue.empty());
    }
    
    public ImplementQueueusingStacks() {
        stack1=new Stack<Integer>();
        stack2=new Stack<Integer>();
    }
    
     /** Push element x to the back of queue. */
    public void push(int x) {
        stack1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
            int ele=0;
            while(!stack1.isEmpty()) {
                if(stack1.size()==1) {
                    ele=stack1.pop();
                }else
                    stack2.push(stack1.pop());      
            }
            while(!stack2.isEmpty())
                stack1.push(stack2.pop());
            
        return ele;
    }
    
    /** Get the front element. */
    public int peek() {
            int ele=0;
        while(!stack1.isEmpty()) {
            if(stack1.size()==1)
                ele=stack1.peek();
            stack2.push(stack1.pop());
        }
        while(!stack2.isEmpty())
            stack1.push(stack2.pop());
            
        return ele;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack1.isEmpty();
    }
}
```


