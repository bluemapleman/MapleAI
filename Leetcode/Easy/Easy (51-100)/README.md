本博客是个人原创的针对leetcode上的problem的解法，所有solution都基本通过了leetcode的官方Judging，个别未通过的例外情况会在相应部分作特别说明。


欢迎互相交流！

email: tomqianmaple@gmail.com

**后续更多的easy题已经不属于Top Interview Questions**，所以现在就不集中精力去做了，只做到目前的100题左右。

[toc]

# Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:

Could you do it in O(n) time and O(1) space?

- My Answer
```
package easy2;

import java.util.ArrayDeque;
import java.util.Stack;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月28日
 */
public class PalindromeLinkedList
{
    public static void main(String[] args)
    {
        ListNode node1=new ListNode(-129);
        ListNode node2=new ListNode(1232);
        ListNode node3=new ListNode(1232);
        ListNode node4=new ListNode(-129);
        node1.next=node2;node2.next=node3;node3.next=node4;
        System.out.println(isPalindrome(node1));
        
    }
    
    
    
    // If a String is a palindrome, then read it forward or backward would derive same result.
    // Use ArrayDeque
    public static boolean isPalindrome(ListNode head) {
        if(head==null || head.next==null)
            return true;
        ArrayDeque<ListNode> deque=new ArrayDeque<ListNode>();
        
        while(head!=null) {
            deque.add(head);
            head=head.next;
        }
        
        while(deque.size()!=0) {
            if(deque.size()==1) {
                return true;
            }else {
                ListNode front=deque.pollFirst(),back=deque.pollLast();
                    if(front.val==back.val)
                        continue;
                    else
                        return false;
            }
        }
            
        return true;
    }
    
    //This method exceeds time limit;
//  public static boolean isPalindrome(ListNode head) {
//      if(head==null || head.next==null)
//          return true;
//      
//      String str="";
//      
//      long start=System.currentTimeMillis();
//      while(head!=null){
//          str+=head.val+"@";
//          head=head.next;
//      }
//      System.out.println("part1:"+(System.currentTimeMillis()-start)+"s");
//      
//      start=System.currentTimeMillis();
//      
//      str=str.substring(0,str.length()-1);
//      
//      String[] strs=str.split("@");
//      
//      // This part2 and part3 spends most of the time, need improvement
//      System.out.println("part2:"+(System.currentTimeMillis()-start)+"s");
//      
//      str=str.substring(0,str.length()-1);
//      for(int i=0;i<strs.length/2;i++) {
//          if(strs[i].equals(strs[strs.length-i-1]))
//              continue;
//          else
//              return false;
//      }
//      System.out.println("part3:"+(System.currentTimeMillis()-start)+"s");
//
//        return true;
//    }
}

class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
}
```

# Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

            _______6______
           /              \
        ___2__          ___8__
       /      \        /      \
       0      _4       7       9
             /  \
             3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

- My Answer

```
package easy2;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月28日
 */
public class LowestCommonAncestorofaBinarySearchTree
{
//  ___6______
//    /              \
// ___2__          ___8__
///      \        /      \
//0      _4       7       9
//      /  \
//      3   5
    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(6);
        TreeNode left1=new TreeNode(2),left2=new TreeNode(0),left3=new TreeNode(4),left4=new TreeNode(3),left5=new TreeNode(5);
        root.left=left1;left1.left=left2;left1.right=left3;left3.left=left4;left3.right=left5;
        TreeNode right1=new TreeNode(8),right2=new TreeNode(7),right3=new TreeNode(9);
        root.right=right1;right1.left=right2;right1.right=right3;
        System.out.println(lowestCommonAncestor(root, left1, left3).val);
    }
    
    // Since T is a binary search tree, then no two elements are the same value, and values on left sub tree are always smaller than root's value, bigger for right sub trees.
    public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(p==q || p.right==q || p.left==q)
            return p;
        else if(q.left==p || q.right==p)
            return q;
        
        // if two nodes p and q are in same sub tree, then we need to go into lower layer recursively. 
        if(root.val>p.val && root.val>q.val) {
            return lowestCommonAncestor(root.left, p, q);
        }else if (root.val<p.val && root.val<q.val) {
            return lowestCommonAncestor(root.right, p, q);
        // if p and q not in same sub tree, then root is the lowest common ancestor.
        }else {
            return root;
        }
    }
}
```

# Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

- My  Answer

```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月28日
 */
public class DeleteNodeinaLinkedList
{
    public static void main(String[] args)
    {
        ListNode node1=new ListNode(1),node2=new ListNode(2),node3=new ListNode(3),node4=new ListNode(4);
        node1.next=node2;node2.next=node3;node3.next=node4;
        deleteNode(node3);
        deleteNode(node2);
        while(node1!=null) {
            System.out.println(node1.val+" ");
            node1=node1.next;
        }
    }
    
    // It's easy to misunderstand the meaning of "deleting the node" here. However, if given only the node to be deleted, we can only change its value and remove later node. 
     public static void deleteNode(ListNode node) {
         node.val=node.next.val;
         node.next=node.next.next;      
     }
}


```

# Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
```
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
```

Note:

You may assume the string contains only lowercase alphabets.

Follow up:

What if the inputs contain unicode characters? How would you adapt your solution to such case?

- My Answer
```
package easy2;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月28日
 */
public class ValidAnagram
{
    public static void main(String[] args)
    {       
        String s="car";String t="rat";
        System.out.println(isAnagram(s, t));
    }
    
    // Just compare whether two Strings have same letter set and same quantity for every letter
    public static boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
            return false;
        
        
        Map<Character, Integer> map1=getFilledMap(s),map2=getFilledMap(t);
        if(map1.keySet().size()!=map2.keySet().size())
            return false;
        else {
            Set<Character> set=map1.keySet();
            
            for(Character c:set) {
                // Attention!!! Here can't be written like "map2.get(c)==map1.get(c)", because map return Integer object, and "==" means comparing address in memory.
                if(map2.containsKey(c) && map2.get(c).equals(map1.get(c)))
                    continue;
                else
                    return false;
            }
        }
        
        
        
        return true;
    }
    
    public static Map<Character,Integer> getFilledMap(String str){
        Map<Character, Integer> map=new HashMap<Character,Integer>();
        for(int i=0;i<str.length();i++) {
            char key=str.charAt(i);
            if(map.containsKey(key))
                map.put(key, map.get(key)+1);
            else
                map.put(key,1);
        }
        return map;
    }
}

```

# Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

       1
     /   \
    2     3
     \
      5
All root-to-leaf paths are:

["1->2->5", "1->3"]

- My Answer
```
package easy2;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月28日
 */
public class BinaryTreePaths
{
//     1
//   /   \
//  2     3
//   \
//    5
    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(1);
        TreeNode left1=new TreeNode(2),left2=new TreeNode(5);
        root.left=left1;left1.right=left2;
        TreeNode right1=new TreeNode(3);
        root.right=right1;
//      for(String str:binaryTreePaths(root))
//          System.out.println(str);
        System.out.println(binaryTreePaths(root));
    }
    
    public static List<String> binaryTreePaths(TreeNode root) {
        List<String> list=new ArrayList<String>();
        if(root!=null)
            searchBT(root,"",list);
        return list;
    }
    
    // This is the solution offered by vimukthi(https://leetcode.com/problems/binary-tree-paths/discuss/68258)
    private static void searchBT(TreeNode root, String path, List<String> answer) {
        if (root.left == null && root.right == null) answer.add(path + root.val);
        if (root.left != null) searchBT(root.left, path + root.val + "->", answer);
        if (root.right != null) searchBT(root.right, path + root.val + "->", answer);
    }
}


```

# Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class AddDigits
{
    public static void main(String[] args)
    {
        System.out.println(addDigits(3958));
    }
    
    public static int addDigits(int num) {
        int sum=0;
        while(true) {
            while(num/10!=0) {
                int yushu=num%10;
                sum+=yushu;
                num/=10;
            }
            sum+=num;
            if(sum/10==0)
                return sum;
            else {
                num=sum;
                sum=0;
            }
        }   
    }
}
```

# Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

- My Answer

```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class UglyNumber
{
    public static void main(String[] args)
    {
        System.out.println(Integer.MIN_VALUE);
        System.out.println(isUgly(-14));
    }
    
    public static boolean isUgly(int num) {
        if(num<=0)
            return false;
        
        if(num!=1) {
            while(num>1) {
                System.out.println("num："+num);
                if(num/2>0 && num%2==0)
                    num/=2;
                else if(num/3>0 && num%3==0)
                    num/=3;
                else if(num/5>0 && num%5==0)
                    num/=5;
                else
                    return false;
            }
        }
        
        return true;
    }
    
}


```

# Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1
```
Input: [3,0,1]
Output: 2
```
Example 2
```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

Note:

Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class MissingNumber
{
    public static void main(String[] args)
    {
        int[] nums= {0,1,3,4,6,7,8,5,9,10};
        System.out.println(missingNumber(nums));
    }
    
    
    //  The basic idea is to use XOR operation. We all know that a^b^b =a, which means two xor operations with the same number will eliminate the number and reveal the original number.
    //  In this solution, I apply XOR operation to both the index and value of the array. In a complete array with no missing numbers, the index and value should be perfectly corresponding( nums[index] = index), so in a missing array, what left finally is the missing number.
    public static int missingNumber(int[] nums) {
        int xor = 0, i = 0;
        for (i = 0; i < nums.length; i++) {
            xor = xor ^ i ^ nums[i];
        }
        System.out.println(xor+"-"+i);

        return xor ^ i;
    }
}


```


# First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class FirstBadVersion
{
    public static void main(String[] args)
    {
        System.out.println(firstBadVersion(3));
        
    }
    
    
    /* The isBadVersion API is defined in the parent class VersionControl.
    boolean isBadVersion(int version); */
    public static int firstBadVersion(int n) {
        if(isBadVersion(1))
            return 1;
        int middle=n/2;
        int start=1,end=n;
        while(middle>=start && middle<=end) {
            if(isBadVersion(middle)) {
                if(middle==start)
                    if(isBadVersion(start))
                        return start;
                
                if(!isBadVersion(middle-1))
                    return middle;
                
                end=middle;
            }else if(isBadVersion(middle+1))
                return middle+1;
            else
                start=middle;
            middle=(int)(start/2.0+end/2.0);
        }
        return -1;
    }
    
    public static boolean isBadVersion(int n) {
        if(n>=3)
            return true;
        else return false;
    }
}


```


# Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

You must do this in-place without making a copy of the array.

Minimize the total number of operations.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月29日
 */
public class MoveZeroes
{
    public static void main(String[] args)
    {
        int nums[]= {0,1,0,3,12};
        moveZeroes(nums);
        for(int i=0;i<nums.length;i++)
            System.out.println(nums[i]+" ");
    }
    
    public static void moveZeroes(int[] nums) {
        int index=0;
        for(int i=0;i<nums.length;i++) {
                if(nums[i]!=0) {
                    nums[index]=nums[i];
                    index++;
                }
        }
        while(index<nums.length) {
                nums[index]=0;
                index++;
        }
    }
}
```

# Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
```
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
```
Notes:

You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

- My Answer
```
package easy2;

import java.util.HashMap;
import java.util.Map;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月30日
 */
public class WordPattern
{
    public static void main(String[] args)
    {
        System.out.println(wordPattern("abba","dog cat cat dog"));
        System.out.println(wordPattern("abba","dog cat cat fish"));
        System.out.println(wordPattern("abba","dog dog dog dog"));
        System.out.println(wordPattern("aaaa","dog cat cat dog"));
        System.out.println(wordPattern("abc","b c a"));
    }
    public static boolean wordPattern(String pattern, String str) {
        Map<String, String> map=new HashMap<String,String>();
        String[] strs=str.split(" ");
        int len=strs.length;
        
        if(len!=pattern.length())
            return false;
        
        for(int i=0;i<len;i++) {
            String key=String.valueOf(pattern.charAt(i));
            if(map.containsKey(key)) {
                if(!(map.get(key).equals(strs[i])))
                    return false;
            }else {
                if(map.containsValue(strs[i]))
                    return false;
                map.put(key,strs[i]);
            }
        }
        return true;
    }
}
```

# Nim Game

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月31日
 */
public class NimGame
{
    // Just list out some examples, we can soon find that only when n is a multiple of 4, then we will fail the game. 
    // 1t 2t 3t 4f 5t 6t 7t 8f 9t 10t 11t 12f
    public boolean canWinNim(int n) {
        if(n%4==0 && n/4>=1)
            return false;
        
        else return true;
    }
}
```

# Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```
Note:

1.You may assume that the array does not change.

2.There are many calls to sumRange function.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月31日
 */
class RangeSumQueryImmutable {
    
    int[] sums;
    
    public RangeSumQueryImmutable(int[] nums) {
        this.sums=nums;
        
        for(int i=1;i<sums.length;i++) {
                sums[i]=sums[i-1]+sums[i];
        }
        
    }
    
    public int sumRange(int i, int j) {
            if(i==0)
                return sums[j];
            else
                return sums[j]-sums[i-1];
    }
    
    public static void main(String[] args)
    {
            int nums[]= {-2,0,3,-5,2,-1};
        RangeSumQueryImmutable obj=new RangeSumQueryImmutable(nums);
        System.out.println(obj.sumRange(0, 5));
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
```

# Power of Three

Given an integer, write a function to determine if it is a power of three.

Follow up:

Could you do it without using any loop / recursion?

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月31日
 */
public class PowerofThree
{
    // with recursion.
    public boolean isPowerOfThree(int n) {
        if(n==1)
            return true;
        if(n%3==0 && n/3>=1)
            return isPowerOfThree(n/3);
        else
                return false;
    }
}
```

# Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月31日
 */
public class PowerofFour
{
    // withou loop or recursion
    public boolean isPowerOfFour(int num) {
        // 换底公式! log(a,b)=log(c,a)/log(c,b)
        // 判断结果是否为整数即可。
        return (Math.log(num) / Math.log(4)) % 1 == 0; 
    }
}
```

# Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:

Given s = "hello", return "olleh".

- My Answer
```
package easy2;

import java.util.Stack;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class ReverseString
{
    //O(1.5n)
    public String reverseString(String s) {
        char[] arr=s.toCharArray();
        int len=arr.length;
        for(int i=0;i<len/2;i++) {
            char temp=arr[i];
            arr[i]=arr[len-i-1];
            arr[len-i-1]=temp;
        }
        return String.valueOf(arr);
    }
    
    
    // Exceeds time limit: O(2n)
//  public String reverseString(String s) {
//      char[] arr=s.toCharArray();
//      Stack<Character> stack=new Stack<Character>();
//        for(int i=0;i<arr.length;i++) {
//              stack.push(arr[i]);
//        }
//        s="";
//        while(!stack.isEmpty())
//              s+=stack.pop();
//        return s;
//        
//    }
}
```

# Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
```
Given s = "hello", return "holle".
```
Example 2:
```
Given s = "leetcode", return "leotcede".
```
Note:

The vowels does not include the letter "y".

- My Answer
```
package easy2;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class ReverseVowelsofaString
{
    //vowel includes: a o e i u
    public String reverseVowels(String s) {
        Set<Character> vowelSet=new HashSet<Character>();
        vowelSet.add('a');vowelSet.add('o');vowelSet.add('e');vowelSet.add('i');vowelSet.add('u');
        vowelSet.add('A');vowelSet.add('O');vowelSet.add('E');vowelSet.add('I');vowelSet.add('U');
        
        List<Integer> vowelIndexList=new ArrayList<Integer>();
        char[] arr=s.toCharArray();
        for(int i=0;i<arr.length;i++)
            if(vowelSet.contains(arr[i]))
                vowelIndexList.add(i);
        
        int listSize=vowelIndexList.size();
        for(int i=0;i<listSize/2;i++) {
            char temp=arr[vowelIndexList.get(i)];
            arr[vowelIndexList.get(i)]=arr[vowelIndexList.get(listSize-i-1)];
            arr[vowelIndexList.get(listSize-i-1)]=temp;
        }
        
        return String.valueOf(arr);
        
    }
}
```

#  Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:

Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
- Each element in the result must be unique.
- The result can be in any order.

- My Answer

```
package easy2;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class IntersectionofTwoArrays
{
    public static void main(String[] args)
    {
        int[] nums1= {1,2},nums2= {2,1};
        int[] arr=intersection(nums1, nums2);
        for(int i=0;i<arr.length;i++)
            System.out.print(arr[i]+" ");
    }
    
    public static int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1=new HashSet<Integer>(),set2=new HashSet<Integer>();
        for(int i=0;i<nums1.length;i++)
            set1.add(nums1[i]);
        for(int i=0;i<nums2.length;i++)
            set2.add(nums2[i]);
        
        set1.retainAll(set2);
        
        int[] arr=new int[set1.size()];
        int i=0;
        for(Integer ele:set1) {
            arr[i++]=ele;
        }
        return arr;
    }
}
```

# Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
```
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
```
Note:
- Each element in the result should appear as many times as it shows in both arrays.
- The result can be in any order.

Follow up:
- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

- My Answer
```
package easy2;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class IntersectionofTwoArraysII
{
    public static void main(String[] args)
    {
        int[] nums1= {2,2,3,3,1,1,1,1,1},nums2={1,2,2,1,3,1,1,1};
        int[] arr=intersect(nums1, nums2);
        for(int i=0;i<arr.length;i++)
            System.out.print(arr[i]+" ");
                
    }
    public static int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map1=new HashMap<Integer,Integer>(),map2=new HashMap<Integer,Integer>();
        for(int i=0;i<nums1.length;i++)
            if(map1.containsKey(nums1[i]))
                map1.put(nums1[i],map1.get(nums1[i])+1);
            else
                map1.put(nums1[i], 1);
        for(int i=0;i<nums2.length;i++)
            if(map2.containsKey(nums2[i]))
                map2.put(nums2[i],map2.get(nums2[i])+1);
            else
                map2.put(nums2[i], 1);
        
        Set<Integer> keySet1=map1.keySet(),keySet2=map2.keySet();
        Map<Integer, Integer> commonMap=new HashMap<Integer,Integer>();
        
        int size=0;
        for(Integer num:keySet1) {
                if(keySet2.contains(num)) {
                    int quantity=Math.min(map1.get(num), map2.get(num));
                    commonMap.put(num,quantity);
                    size+=quantity;
                }
        }
        
        int[] answer=new int[size];
        Set<Integer> keySet=commonMap.keySet();
        
        
        int index=0;
        for(Integer key:keySet) {
                int quantity=commonMap.get(key);
                for(int i=0;i<quantity;i++)
                    answer[index++]=key;
        }
        
        return answer;
        
    }
}
```

# Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
```
Input: 16
Returns: True
```
Example 2:
```
Input: 14
Returns: False
```

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class ValidPerfectSquare
{
    public boolean isPerfectSquare(int num) {
        int i=1,temp;
        while(true) {
            temp=i*i;
            if(temp==num)
                return true;
            else if(temp<num) {
                if(!((i+1)*(i+1)>temp)) {
                    return false;
                }
            }else
                return false;
            i++;
        }
    }
}
```

# Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:

Given a = 1 and b = 2, return 3.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class SumofTwoIntegers
{
    public static void main(String[] args)
    {
        int num=3;
        String str1=Integer.toBinaryString(num);
        String str2=Integer.toBinaryString(num-1);
        System.out.println("str1:"+str1+",str2:"+str2);
        String result=Integer.toBinaryString(num&(num-1));
        System.out.println("result:"+result);
        
        int count=0;
        while(num!=0) {
            num = num&(num-1);
            count++;
        }
        System.out.println("count:"+count);
    }
    
    // solution from https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
    // Above is a very excellent explanation for various fantastic application of bit manipulation!!!
    
    //  Use ^ to remove even exactly same numbers and save the odd, or save the distinct bits and remove the same.
    //
    //  Sum of Two Integers
    //  Use ^ and & to add two integers
    public static int getSum(int a, int b) {
        // ^ plays a role of adding distinct bits to a [temp], while & plays a role of transferring carry to another number to be added to [temp]
        // When b is equal to 0, then it means there is no carry, and all bits added correctly.
        
        return b==0? a:getSum(a^b, (a&b)<<1); //be careful about the terminating condition;
    }
}
```

# Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
```
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
```
Example:
```
n = 10, I pick 6.

Return 6.
```

- My Answer
```
package easy2;

import java.util.Arrays;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class GuessNumberHigherorLower
{
    public static int answer=2;
    
    public static void main(String[] args)
    {
        System.out.println(guessNumber(2));
    }
    
    /* The guess API is defined in the parent class GuessGame.
       @param num, your guess
       @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
          int guess(int num); */

    // A variant of binary search.
    public static int guessNumber(int n) {
            int start=1,end=n;
            int guess=(int)(start/2.0+end/2.0);
            while(start<end) {
                int guessResult=guess(guess);
                if(guessResult==1) {
                    start=guess+1;
                    guess=(int)(start/2.0+end/2.0);
                }else if(guessResult==-1) {
                    end=guess-1;
                    guess=(int)(start/2.0+end/2.0);
                }else
                    return guess;
            }
            return guess;
    }
    
    public static int guess(int num) {
            if(answer>num)
                return 1;
            else if(answer==num)
                return 0;
            else
                return -1;
    }
}
```

# Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:

You may assume that both strings contain only lowercase letters.
```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

- My Answer
```
package easy2;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class RansomNote
{
    public static void main(String[] args)
    {
        String ransomNote="abcdefggtt",magazine="ipouoewirpoipobbaaddeeffccghgit";
        System.out.println(canConstruct(ransomNote, magazine));
    }
    
    public static boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> ransomMap=new HashMap<Character, Integer>();
        char[] ransomArr=ransomNote.toCharArray();
        for(int i=0;i<ransomArr.length;i++) {
            Character key=ransomArr[i];
            if(ransomMap.containsKey(key))
                ransomMap.put(key, ransomMap.get(key)+1);
            else 
                ransomMap.put(key, 1);
        }
        
        Set<Character> set=ransomMap.keySet();
        
        for(Character c:set) {
            int quantity=ransomMap.get(c);
            int fromIndex=0;
            for(int i=0;i<quantity;i++) {
                int index=magazine.indexOf(c, fromIndex);
                if(index==-1) {
                    return false;
                }else {
                    fromIndex=index+1;
                }
            }
        }
        
        return true;
    }
}
```

# First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```
Note: You may assume the string contain only lowercase letters.

- My Answer
```
package easy2;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月2日
 */
public class FirstUniqueCharacterinaString
{
    public static void main(String[] args)
    {
        System.out.println(firstUniqChar("leetcode"));
        System.out.println(firstUniqChar("aadd"));
    }
    
    public static int firstUniqChar(String s) {
        Set<Character> set=new HashSet<Character>();
        char uniqChar='@';
        int len=s.length();
        for(int i=0;i<len;i++) {
            char c=s.charAt(i);
            if(!set.contains(c)){
                if(s.indexOf(c,i+1)!=-1) {
                    set.add(c);
                }else {
                    uniqChar=c;
                    break;
                }
            }
        }
        return s.indexOf(uniqChar);
    }
}
```

# Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:
```
Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
```

- My Answer
```
package easy2;

import java.util.HashMap;
import java.util.Map;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月5日
 */
public class FindtheDifference
{
    public static void main(String[] args)
    {
        System.out.println(findTheDifference("", "b"));
    }
    
    public static char findTheDifference(String s, String t) {
        Map<Character,Integer> maps=new HashMap<Character,Integer>(),mapt=new HashMap<Character,Integer>();
        char[] arrs=s.toCharArray(),arrt=t.toCharArray();
        for(int i=0;i<arrs.length;i++) {
            char key=arrs[i];
            if(maps.containsKey(key))
                maps.put(key, maps.get(key)+1);
            else
                maps.put(key, 1);
        }
        
        for(int i=0;i<arrt.length;i++) {
            char key=arrt[i];
            if(mapt.containsKey(key))
                mapt.put(key, mapt.get(key)+1);
            else
                mapt.put(key, 1);
        }
        
        // if add a character that doesn't exist in s, then key sets of respective map for string s and t differ in size
        // else differ in certain value for key.
        
        if(mapt.keySet().size()!=maps.keySet().size()) {
            mapt.keySet().removeAll(maps.keySet());
            for(Character key:mapt.keySet())
                return key;
        }
        else {
            for(Character key:mapt.keySet()) {
                if(maps.get(key).compareTo(mapt.get(key))!=0)
                    return key;
            }
        }
        
        return 0;
    }
}
```

# Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
```
Input:
3

Output:
3
```
Example 2:
```
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10. 
```

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月5日
 */
public class NthDigit
{
    public static void main(String[] args)
    {
        //1234567891011
        System.out.println(findNthDigit(9));
        System.out.println(findNthDigit(10));
        System.out.println(findNthDigit(11));
        System.out.println(findNthDigit(12));
        System.out.println(findNthDigit(13));
        System.out.println(findNthDigit(14));
        System.out.println(findNthDigit(15));
        
    }
    public static int findNthDigit(int n) {
        // digit sum from 1 to n: 9*10^0*1+9*10^1*2+9*10^2*3+... =9+90+900*3+...=9*(1*1+10*2+100*3)
        
        int temp=n,digitRange=0;
        
        for(int i=0;i<100;i++) {
            int digitRangeNum=(int)(9*Math.pow(10, i)*(i+1));
            if(temp<=digitRangeNum) {
                digitRange=i+1;
                break;
            }else{
                temp-=digitRangeNum;
            }
        }
        
        int digitNum=temp/digitRange;
        int yushu=temp%digitRange;
        if(yushu==0) {
            return ((int)Math.pow(10, digitRange-1)+digitNum-1)%10;
        }else {
            int number=(int)Math.pow(10, digitRange-1)+digitNum;
            for(int i=0;i<digitRange-yushu;i++) {
                number/=10;
            }
            return number%10;
        }
    }
}
```

# Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:
```
    3
   / \
  9  20
    /  \
   15   7
```
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

- My Answer

```
package easy2;

import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月5日
 */
public class SumofLeftLeaves
{
    public int sumOfLeftLeaves(TreeNode root) {
        if(root==null)
            return 0;
        
        int result=0;
        if(root.left!=null && root.left.left==null && root.left.right==null)
            result+=root.left.val;
        
        return result+sumOfLeftLeaves(root.left)+sumOfLeftLeaves(root.right);
    }
}
```

# Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
```
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
```

- My Answer
```
package easy2;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class LongestPalindrome
{
    public int longestPalindrome(String s) {
        if(s.length()<=1)
            return s.length();
        
        Map<Character, Integer> map=new HashMap<Character,Integer>();
        char[] arr=s.toCharArray();
        for(int i=0;i<arr.length;i++) {
            char key=arr[i];
            if(map.containsKey(key))
                map.put(key, map.get(key)+1);
            else
                map.put(key,1);
        }
        
        Set<Character> set=map.keySet();
        int doubleCharNum=0;
        boolean oneMoreCharFlag=false;
        for(Character key:set) {
            if(map.get(key)%2==0)
                doubleCharNum+=map.get(key);
            else {
                doubleCharNum+=map.get(key)-1;
                oneMoreCharFlag=true;
            }
        }
        if(oneMoreCharFlag)
            doubleCharNum+=1;
        
        return doubleCharNum;
    }
}
```

#  Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
```
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

- My Answer
```
package easy2;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class FizzBuzz
{
    public List<String> fizzBuzz(int n) {
        List<String> list=new ArrayList<String>();
        for(int i=1;i<=n;i++) {
            if(i%15==0)
                list.add("FizzBuzz");
            else if(i%3==0)
                list.add("Fizz");
            else if(i%5==0)
                list.add("Buzz");
            else
                list.add(""+i);
        }
        return list;
    }
}
```

# Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
```
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
```
Example 2:
```
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
```
Example 3:
```
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```

- My Answer
```
package easy2;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class ThirdMaximumNumber
{
    public static void main(String[] args)
    {
        System.out.println(Integer.MIN_VALUE);
    }
    public int thirdMax(int[] nums) {
        int[] maxThreeArr= {Integer.MIN_VALUE,Integer.MIN_VALUE,Integer.MIN_VALUE};
        
        
        for(int i=0;i<nums.length;i++) {
            int ele=nums[i];
            
            if(ele==maxThreeArr[2] || ele==maxThreeArr[1] || ele==maxThreeArr[0])
                continue;
            if(ele>maxThreeArr[2]) {
                maxThreeArr[0]=maxThreeArr[1];
                maxThreeArr[1]=maxThreeArr[2];
                maxThreeArr[2]=ele;
            }
            else if(ele>maxThreeArr[1]) {
                maxThreeArr[0]=maxThreeArr[1];
                maxThreeArr[1]=ele;
            }
            else if(ele>maxThreeArr[0])
                maxThreeArr[0]=ele;
        }
        
        // Judge whether there are at least three different numbers in array
        boolean threeNumFlag=false;
        Set<Integer> set=new HashSet<Integer>();
        for(int i=0;i<nums.length;i++) {
            set.add(nums[i]);
            if(set.size()>=3) {
                threeNumFlag=true;
                break;
            }
        }
        
        if(threeNumFlag)
            return maxThreeArr[0];
        else
            return maxThreeArr[2];
    }
}
```

# Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

1.The length of both num1 and num2 is < 5100.

2.Both num1 and num2 contains only digits 0-9.

3.Both num1 and num2 does not contain any leading zero.

4.You must not use any built-in BigInteger library or convert the inputs to integer directly.

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class AddStrings
{
    public String addStrings(String num1, String num2) {
        int len1=num1.length(),len2=num2.length();
        int len=Math.max(len1, len2);
        if(len>len2)
            for(int i=0;i<len-len2;i++)
                num2="0"+num2;
        else 
            for(int i=0;i<len-len1;i++)
                num1="0"+num1;
        
        StringBuilder result=new StringBuilder("");
        
        boolean jinwei=false;
        for(int i=0;i<len;i++) {
            char c1=num1.charAt(len-i-1),c2=num2.charAt(len-i-1);
            int sum=Character.digit(c1, 10)+Character.digit(c2, 10);
            sum=jinwei?sum+1:sum;
            if(sum>=10)
                jinwei=true;
            else
                jinwei=false;
            result.append(sum%10);
        }
        
        if(jinwei)
            result.append("1");
        
        return result.reverse().toString();
    }
}
```

# Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
```
Input: "Hello, my name is John"
Output: 5
```

- My Answer
```
package easy2;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class NumberofSegmentsinaString
{
    public int countSegments(String s) {
        if(s.length()==0)
            return 0;
        
        int result=0;
        
        String regex="\\S+";
        Pattern pattern=Pattern.compile(regex);
        Matcher matcher=pattern.matcher(s);
        while(matcher.find()) {
            result++;
        }
        return result;
    }
}
```

# Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

- My Answer
```
package easy2;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class PathSumIII
{
    // solution from https://leetcode.com/problems/path-sum-iii/discuss/91889/Simple-Java-DFS
    // DFS Thought
    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        return pathSumFrom(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
    }
    
    private int pathSumFrom(TreeNode node, int sum) {
        if (node == null) return 0;
        return (node.val == sum ? 1 : 0) 
            + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val);
    }
}
```

# Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```
Example 2:
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

- My Answer
```
package easy2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class FindAllAnagramsinaString
{
    public List<Integer> findAnagrams(String s, String p) {
        int lens=s.length(),lenp=p.length();
        List<Integer> list=new ArrayList<Integer>();
        
        if(lens<lenp)
            return list;

        Map<Character,Integer> maps=new HashMap<Character,Integer>(),mapp=new HashMap<Character,Integer>();
        char[] pArr=p.toCharArray();
        char[] sArr=s.toCharArray();
        for(int i=0;i<pArr.length;i++) {
            // for p's map
            char key=pArr[i];
            if(mapp.containsKey(pArr[i]))
                mapp.put(key, mapp.get(key)+1);
            else
                mapp.put(key, 1);
            // for s's map
            key=sArr[i];
            if(maps.containsKey(sArr[i]))
                maps.put(key, maps.get(key)+1);
            else
                maps.put(key, 1);
        }
        
        if(judgeSameMap(maps, mapp))
            list.add(0);
        
        for(int i=0;i<lens-lenp;i++) {
            char removeChar=sArr[i],addChar=sArr[i+lenp];
            maps.put(removeChar, maps.get(removeChar)-1);
            if(maps.get(removeChar)==0)
                maps.remove(removeChar);
            if(maps.containsKey(addChar))
                maps.put(addChar,maps.get(addChar)+1);
            else
                maps.put(addChar,1);
            
            if(judgeSameMap(maps, mapp))
                list.add(i+1);
        }
        
        return list;
    }
    
    public boolean judgeSameMap(Map<Character,Integer> map1,Map<Character,Integer> map2) {
        Set<Character> set1=map1.keySet(),set2=map2.keySet();
        if(set1.size()!=set2.size())
            return false;
        else {
            for(Character key:set1) {
                if(!set2.contains(key))
                    return false;
                if(map1.get(key).compareTo(map2.get(key))!=0)
                    return false;
            }
        }
        return true;
    }
}
```

# Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
```
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
```
Example 2:
```
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
```

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月6日
 */
public class ArrangingCoins
{
    public int arrangeCoins(int n) {
        if(n<=1)
            return n;
        int temp=n;
        for(int i=1;i<=n;i++) {
            if(temp<i) {
                return i-1;
            }else
                temp-=i;
        }
        return -1;
    }
}
```


# String Compression

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:

Could you solve it using only O(1) extra space?


Example 1:
```
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
```
Example 2:
```
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
```
Example 3:
```
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
```
Note:
- All characters have an ASCII value in [35, 126].
- 1 <= len(chars) <= 1000.



- My Answer (This answer didn't pass the examination, but I think the result is the same as the reference, so I still leave my answer here.)
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月7日
 */
public class StringCompression
{
    public int compress(char[] chars) {
        char beforeChar='@';
        int index=0;
        int count=1;
        for(int i=0;i<chars.length;i++) {
            char presentChar=chars[i];
            for(int j=0;j<chars.length;j++) {
                System.out.print(chars[j]);
            }
            System.out.println();
            System.out.println("before:"+beforeChar+",present:"+presentChar);
            System.out.println();
            
            if(beforeChar!='@') {
                // next char is the same as present char 
                if(beforeChar==presentChar) {
                    count++;
                    if(i==chars.length-1) {
                        fillCharArr(chars, index, count);
                        break;
                    }
                }else {
                    // put number after char
                    if(count==1) {
                        beforeChar=presentChar;
                        index++;
                        continue;
                    }else if(count<10) {
                        chars[++index]=Character.forDigit(count, 10);
                    }else {
                        index+=fillCharArr(chars,index, count)+1;
                    }
                    
                    chars[++index]=presentChar;
                    count=1;
                    beforeChar=presentChar;
                    if(i==chars.length-1) {
                        if(count!=1)
                            chars[++index]=chars[i];
                    }
                }
            }else{ // first char
                beforeChar=presentChar;
            }
        }
        for(int j=0;j<chars.length;j++) {
            System.out.print(chars[j]);
        }
        return index;
    }
    
    // return number of count chars
    public int fillCharArr(char[] chars,int start,int count) {
        if(count==1)
            return 1;
        int temp=count;
        // attention: number of char must be filled in order from left to right
        // so we first need to know how many digits are in number
        int digitNum=0;
        while(temp!=0) {
            digitNum++;
            temp/=10;
        }
        temp=count;
        for(int j=0;j<digitNum;j++) {
            int yushu=temp%10;
            chars[start+digitNum-j]=Character.forDigit(yushu, 10);
            temp/=10;
        }
        return digitNum;
    }
    
//  public int compress(char[] chars) {
//      Map<Character, Integer> map=new HashMap<Character,Integer>();
//      for(int i=0;i<chars.length;i++) {
//          char key=chars[i];
//          if(map.containsKey(key))
//              map.put(key, map.get(key)+1);
//          else
//              map.put(key, 1);
//      }
//      
//      int answer=0;
//      Set<Character> set=map.keySet();
//      for(Character key:set) {
//          int value=map.get(key);
//          if(value==1)
//              chars[answer++]=key;
//          else {
//              chars[answer]=key;
//              if(value>=10) {
//                  int temp=value;
//                  // attention: number of char must be filled in order from left to right
//                  // so we first need to know how many digits are in number
//                  int digitNum=0;
//                  while(temp!=0) {
//                      digitNum++;
//                      temp/=10;
//                  }
//                  temp=value;
//                  for(int i=0;i<digitNum;i++) {
//                      int yushu=temp%10;
//                      chars[answer+digitNum-i]=Character.forDigit(yushu, 10);
//                      temp/=10;
//                  }
//                  answer+=digitNum+1;
//              }else {
//                  chars[answer+1]=Character.forDigit(value,10);
//                  answer+=2;
//              }
//              
//          }
//          for(int i=0;i<chars.length;i++)
//              System.out.print(chars[i]);
//          System.out.println();
//      }
//        return answer;
//    }
}
```

# Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
```
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
```

- My Answer
```
package easy2;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月8日
 */
public class NumberofBoomerangs
{   
    // First build a matrix that contains all distance data between pairwise points.
    // Then iterate over every point to see how many other points have the same distance from it, and count them all;
    public static int numberOfBoomerangs(int[][] points) {
        int count=0;
        
        int rows=points.length,columns=points[0].length;
        
        double[][] distanceMatrix=new double[rows][rows];
        for(int i=0;i<rows;i++) {
                int[] currentPoint=points[i];
                for(int j=i+1;j<rows;j++) {
                    double distance=getDistance(currentPoint, points[j]);
                    distanceMatrix[i][j]=distance;
                    distanceMatrix[j][i]=distance;
                }
        }
        
        
        
        for(int i=0;i<rows;i++) {
                Map<Double, Integer> distanceMap=new HashMap<Double,Integer>();
                for(int j=0;j<rows;j++) {
                    double key=distanceMatrix[i][j];
                    if(distanceMap.containsKey(key)) {
                        distanceMap.put(key, distanceMap.get(key)+1);
                    }else
                        distanceMap.put(key, 1);
                }
                for(Double distance:distanceMap.keySet()) {
                    int value=distanceMap.get(distance);
                    if(value>=2) {
                        count+=getCombination(value, 2)*2;
                    }
                }
        }
        
        return count;
    }
    
    public static double getDistance(int[] point1,int[] point2) {
        return Math.sqrt(Math.pow(point1[0]-point2[0], 2)+Math.pow(point1[1]-point2[1], 2));
    }
    
    public static int getCombination(int m,int n) {
        BigInteger denominator=new BigInteger("1"),numerator=new BigInteger("1");
        int temp=n;
        while(temp-->0) {
            numerator=numerator.multiply(BigInteger.valueOf(m--));
        }
        temp=n;
        while(temp-->0) {
            denominator=denominator.multiply(BigInteger.valueOf(n--));
        }
        
        return numerator.divide(denominator).intValue();
    }
}
```

#  Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```

- My Answer
```
package easy2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月8日
 */
public class FindAllNumbersDisappearedinanArray
{
    // This solution from: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92956/Java-accepted-simple-solution
    //   The basic idea is that we iterate through the input array and mark elements as negative using nums[nums[i] -1] = -nums[nums[i]-1]. 
    //   In this way all the numbers that we have seen will be marked as negative. In the second iteration, if a value is not marked as negative, 
    //   it implies we have never seen that index before, so just add it to the return list.
    public List<Integer> findDisappearedNumbers(int[] nums) {
           List<Integer> ret = new ArrayList<Integer>();
            
            for(int i = 0; i < nums.length; i++) {
                int val = Math.abs(nums[i]) - 1;
                if(nums[val] > 0) {
                    nums[val] = -nums[val];
                }
            }
            
            for(int i = 0; i < nums.length; i++) {
                if(nums[i] > 0) {
                    ret.add(i+1);
                }
            }
            return ret;
    }
}
```

# Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月9日
 */
public class MinimumMovestoEqualArrayElements
{
    // This solution from: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93815/Java-O(n)-solution.-Short.
//  Adding 1 to n - 1 elements is the same as subtracting 1 from one element, w.r.t goal of making the elements in the array equal.
//  So, best way to do this is make all the elements in the array equal to the min element.
//  sum(array) - n * minimum
    public int minMoves(int[] nums) {
        if (nums.length == 0) return 0;
        int min = nums[0];
        for (int n : nums) min = Math.min(min, n);
        int res = 0;
        for (int n : nums) res += n - min;
        return res;
    }
}
```

# Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
```
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```

- My Answer
```
package easy2;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月9日
 */
public class HammingDistance
{
    public static void main(String[] args)
    {
        System.out.println(hammingDistance(1,4));
    }
    public static int hammingDistance(int x, int y) {
        String xStr=Integer.toBinaryString(x),yStr=Integer.toBinaryString(y);
        int times=Math.max(xStr.length(), yStr.length());
        if(times==xStr.length())
            for(int i=0;i<times;i++)
                yStr="0"+yStr;
        else
            for(int i=0;i<times;i++)
                xStr="0"+xStr;
        int answer=0;
        for(int i=0;i<times;i++) {
            if(xStr.charAt(xStr.length()-i-1)!=yStr.charAt(yStr.length()-i-1))
                answer++;
        }
        return answer;
    }
}
```

# Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
```
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
```
![](https://leetcode.com/static/images/problemset/island.png)

- My Answer
```
package easy2;

import com.mysql.fabric.xmlrpc.base.Array;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年2月9日
 */
public class IslandPerimeter
{
    public static void main(String[] args)
    {
        int[][] grid= {{0,1}};
        for(int i=0;i<grid.length;i++) {
            for(int j=0;j<grid[0].length;j++) {
                System.out.print(grid[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println(islandPerimeter(grid));
    }
    
    // this solution from: https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution
//  loop over the matrix and count the number of islands;
//  if the current dot is an island, count if it has any right neighbour or down neighbour;
//  the result is islands * 4 - neighbours * 2
    public static int islandPerimeter(int[][] grid) {
        int islands = 0, neighbours = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    islands++; // count islands
                    if (i < grid.length - 1 && grid[i + 1][j] == 1) neighbours++; // count down neighbours
                    if (j < grid[i].length - 1 && grid[i][j + 1] == 1) neighbours++; // count right neighbours
                }
            }
        }

        return islands * 4 - neighbours * 2;
    }
    
    // This solution exceeds time limit;
    // add a new 1-block thick boundary to original grid, then count quantity of 0 around 1 for each 1; the same 0 can be counted more than once
//  public static int islandPerimeter(int[][] grid) {
//      int answer=0;
//      
//      
//      if(grid.length==1 || grid[0].length==1) {
//          int count=0;
//          for(int i=0;i<grid.length;i++) {
//              for(int j=0;j<grid[0].length;j++) {
//                  if(grid[i][j]==1) {
//                      count++;
//                  }
//              }
//          }
//          return count*2+2;
//      }
//      
//      for(int i=0;i<grid.length;i++) {
//          for(int j=0;j<grid[0].length;j++) {
//              System.out.print(grid[i][j]+" ");
//              if(grid[i][j]==1) {
//                  if(i==0 && j!=0 && j!=grid[0].length-1) {
//                      answer++;
//                      if(grid[i+1][j]==0)
//                          answer++;
//                      if(grid[i][j-1]==0)
//                          answer++;
//                      if(grid[i][j+1]==0)
//                          answer++;
//                  }else if(i==grid.length-1 && j!=0 && j!=grid[0].length-1) {
//                      answer++;
//                      if(grid[i-1][j]==0)
//                          answer++;
//                      if(grid[i][j-1]==0)
//                          answer++;
//                      if(grid[i][j+1]==0)
//                          answer++;
//                  }else if(j==0 && i!=0 && i!=grid.length-1) {
//                      answer++;
//                      if(grid[i-1][j]==0)
//                          answer++;
//                      if(grid[i+1][j]==0)
//                          answer++;
//                      if(grid[i][j+1]==0)
//                          answer++;
//                  }else if(j==grid[0].length-1 && i!=0 && i!=grid.length-1) {
//                      answer++;
//                      if(grid[i-1][j]==0)
//                          answer++;
//                      if(grid[i+1][j]==0)
//                          answer++;
//                      if(grid[i][j-1]==0)
//                          answer++;
//                  }
//                  else if(i==0 && j==0){
//                      answer++;answer++;
//                      if(grid[i+1][j]==0)
//                          answer++;
//                      if(grid[i][j+1]==0)
//                          answer++;
//                  }else if(i==0 && j==grid[0].length-1){
//                      answer++;answer++;
//                      if(grid[i+1][j]==0)
//                          answer++;
//                      if(grid[i][j-1]==0)
//                          answer++;
//                  }else if(i==grid.length-1 && j==0){
//                      answer++;answer++;
//                      if(grid[i-1][j]==0)
//                          answer++;
//                      if(grid[i][j+1]==0)
//                          answer++;
//                  }else if(i==grid.length-1 && j==grid[0].length-1){
//                      answer++;answer++;
//                      if(grid[i-1][j]==0)
//                          answer++;
//                      if(grid[i][j-1]==0)
//                          answer++;
//                  }
//                  else {
//                      if(grid[i-1][j]==0)
//                          answer++;
//                      if(grid[i+1][j]==0)
//                          answer++;
//                      if(grid[i][j-1]==0)
//                          answer++;
//                      if(grid[i][j+1]==0)
//                          answer++;
//                  }
//              }
//          }
//          System.out.println();
//      }
//      return answer;
//    }
}
```

# 
