本博客是个人原创的针对leetcode上的problem的解法，所有solution都基本通过了leetcode的官方Judging，个别未通过的例外情况会在相应部分作特别说明。


欢迎互相交流！

email: tomqianmaple@gmail.com

[toc]

# Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

- My Answer
```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int firstIndex=-1,secondIndex=-1;
        
        for(int i=0;i<nums.length;i++){
            int firstEle=nums[i];
            for(int j=i+1;j<nums.length;j++){
                int secondEle=nums[j];
                if(firstEle+secondEle==target){
                    firstIndex=i;
                    secondIndex=j;
                }
            }
        }
        
        int []arr=new int[2];
        arr[0]=firstIndex;
        arr[1]=secondIndex;
        return arr;
    }
}
```


# Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
```
Input: 123
Output:  321
```
Example 2:
```
Input: -123
Output: -321
```
Example 3:
```
Input: 120
Output: 21
```
Note:

Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


- My Answer

```
class Solution{
    public int reverse(int x){
        if(x==0)
            return 0;
        if(x==Integer.MIN_VALUE)
                return 0;
        int reversePart=x;
        // consider minus
        if(x<0)
            reversePart=-x;
        List<Integer> list=new ArrayList<Integer>();
        while(reversePart!=0){
            int yushu=reversePart%10;
            reversePart/=10;
            list.add(yushu);
        }
        
        //if reversed number starts with 0(s),remove them first
        while(list.get(0)==0) {
                list.remove(0);
        }
        int sum=0;
        for(int index=0;index<list.size();index++){
            System.out.println("sum:"+sum);
                if(sum>Integer.MAX_VALUE/10)
                    return 0;
                sum*=10;
            sum+=list.get(index);
        }
        
        if(x<0)
              return -sum;
        return sum;
    }
}
```


# Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.


Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

- My Answer

```
package easy;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月9日
 */
public class PalindromeNumber
{
    public static void main(String[] args)
    {
        System.out.println(isPalindrome(123));

    }
    
    public static boolean isPalindrome(int x) {
        if(x==0)
            return true;
        if(x<0)
            return false;
        List<Integer> list=new ArrayList<Integer>();
        int reversePart=x;
        while(reversePart!=0){
            int yushu=reversePart%10;
            reversePart/=10;
            list.add(yushu);
        }
        //if reversed number starts with 0, it can't be a palindrome number
        if(list.get(0)==0)
                return false;
        
        int sum=0;
        for(int index=0;index<list.size();index++){
                if(sum>Integer.MAX_VALUE/10)
                    return false;
                sum*=10;
            sum+=list.get(index);
        }
        
        if(sum!=x)
                return false;
        
        return true;
    }

}
```

# 13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

- My Answer

```
package easy;

import java.util.HashMap;
import java.util.Map;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月9日
 */
public class RomanToInteger
{

    public static void main(String[] args)
    {
        
        
        System.out.println(romanToInt("CXLXXIV"));
        

    }
    
     public static int romanToInt(String s) {
        Map<String, Integer> map=new HashMap<String, Integer>();
        map.put("I",1);
        map.put("V",5);
        map.put("X",10);
        map.put("L",50);
        map.put("C",100);
        map.put("D",500);
        map.put("M",1000);
        
        if(s.length()==1)
            return map.get(s);
        
        int sum=0;
        int partSum=0;
        for(int i=0;i<s.length();i++) {
            String single=s.substring(i,i+1);
            if(partSum==0)
                partSum+=map.get(single);
            for(int j=i+1;j<s.length();j++,i++) {
                String afterSingle=s.substring(j,j+1);
                //It's a 4 or 9
                if(map.get(afterSingle)>map.get(single)) {
                    partSum=map.get(afterSingle)-partSum;
                    i++;
                    break;
                }
                // keep on adding
                else if(map.get(afterSingle)==map.get(single)) {
                    partSum+=map.get(single);
                    continue;
                }
                else {
                    break;
                }
            }
            System.out.println("sum:"+sum+",partSum:"+partSum);
            sum+=partSum;
            partSum=0;
        }
        
        return sum;
     }

}
```

# Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月9日
 */
public class LongestCommonPrefix
{
    public static void main(String[] args)
    {
        String[] test={"abcsdfsd","abcserwer","abcwedsda","aberger"};
        System.out.println(longestCommonPrefix(test));

    }
    
    public static String longestCommonPrefix(String[] strs) {
        
        if(strs.length==0)
            return "";
        
        // First find the element string that has shortest length, and then iterate from index-[0] until there there were any difference between these strings
        // If iteration continue until the index-[shortestString.length()-1], then shortest string is answer
        
        int minLen=Integer.MAX_VALUE;
        for(String str:strs) {
            // if any string is "", then answer is "";
            if(str.length()==0)
                return "";
            if(str.length()<minLen)
                minLen=str.length();
        }
        
        String commonPrefix="";
        for(int i=0;i<minLen;i++) {
            String single=strs[0].substring(i, i+1);
            for(int j=1;j<strs.length;j++) {
                if(strs[j].substring(i,i+1).equals(single))
                    continue;
                else
                    return commonPrefix;
            }
            commonPrefix+=single;
        }
        
        return commonPrefix;
    }

}

```

# Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月9日
 */
public class ValidParentheses
{   
    public static void main(String[] args)
    {
        System.out.println(isValid("[}[[(){}]][{([])}]{[([()])]}"));

    }
    
    //remove "()","{}","[]" gradually, if anything left, then it must be not valid +_+!
    public static boolean isValid(String s) {
        if(s.length()==0)
          return true;
        if(s.length()%2!=0)
          return false;
        
        String[] groups= {"()","[]","{}"};
        while(true) {
                boolean hasReplace=false;
            for(String group:groups) {
                    String newS=s.replace(group,"");
                    if(newS.length()<s.length()) {
                        hasReplace=true;
                        s=newS;
                    }
            }
            if(hasReplace==false)
                    break;
        }
        if(s.length()!=0)
                return false;
        
        return true;
    }
}
```


# Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月10日
 */

/*
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class MergeTwoSortedLists
{

    public static void main(String[] args)
    {
        ListNode node1=new ListNode(1),node2=new ListNode(2),node3=new ListNode(4);
        node1.next=node2;node2.next=node3;
        ListNode node4=new ListNode(1),node5=new ListNode(3),node6=new ListNode(4);
        node4.next=node5;node5.next=node6;
        ListNode head=mergeTwoLists(node1, node4);
        while(head!=null) {
            System.out.println(head.val);
            head=head.next;
        }
    }
    
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null) {
            return l2;
        }
        if(l2==null){
            return l1;
        }
        ListNode head,temp;
        if(l1.val>l2.val) {
            head=l2;
            l2=l2.next;
        }
        else {
            head=l1;
            l1=l1.next;
        }
        
        temp=head;
        while(l1!=null && l2!=null) {
            if(l1.val>l2.val) {
                temp.next=l2;
                temp=temp.next;
                l2=l2.next;
            }
            else {
                temp.next=l1;
                temp=temp.next;
                l1=l1.next;
            }
        }
        
        if(l1!=null) {
            while(l1!=null) {
                temp.next=l1;
                l1=l1.next;
                temp=temp.next;
            }
        }
        else {
            while(l2!=null) {
                temp.next=l2;
                l2=l2.next;
                temp=temp.next;
            }
        }
        
        return head;
    }

}

class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
}
```


# Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
```

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月10日
 */
public class RemoveDuplicatesFromSortedArray
{

    public static void main(String[] args)
    {
        int[] nums= {1,1,2,2,3,4,4};
        System.out.println(removeDuplicates(nums));
        for(int i=0;i<nums.length;i++) {
            System.out.print(nums[i]+" ");
        }
    }
    
    public static int removeDuplicates(int[] nums) {
        if(nums.length==0)
            return 0;
        
        int count=1;
        
        int beforeEle=nums[0];
        
        for(int i=0;i<nums.length-1;i++) {
            if(nums[i+1]!=beforeEle) {
                count++;
                beforeEle=nums[i+1];
                nums[count-1]=beforeEle;
            }
            else{
                continue;
            }
        }
        
        return count;
    }
}


```


# Remove Element

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
```

- My Answer

**很奇怪，这个答案没通过，但是输出结果确实是对的，可能是我哪里还理解错了，还是把我的答案留在这儿。**


```
package easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月10日
 */
public class RemoveElement
{
    public static void main(String[] args)
    {
        int[] nums= {3,2,2,3};
        System.out.println(removeElement(nums,3));
        for(int i=0;i<nums.length;i++) {
            System.out.print(nums[i]+" ");
        }

    }
    
    public static int removeElement(int[] nums, int val) {
        
        if(nums.length==0)
            return 0;
        
        Arrays.sort(nums);
        int start=0;
        int end=0;
        for(int i=0;i<nums.length;i++) {
            if(nums[i]==val) {
                start=i;
                break;
            }
        }
        
        end=start;
        for(int i=start+1;i<nums.length;i++) {
            if(nums[i]==val)
                end++;
            else
                break;
        }
        int count=0;
        
        if(count==0){
            return nums.length;
        }
        
        count=end-start+1;
        
        for(int i=end+1;i<nums.length;i++) {
            nums[i-count]=nums[i];
        }
        
        return nums.length-count;
        
    }
    
    // This answer exceeds time limit
//  public int removeElement(int[] nums, int val) {
//        int count=0;
//      for(int i=0;i<nums.length;i++)
//          if(nums[i]==val)
//              count++;
//      for(int i=0;i<nums.length;i++) {
//          if(nums[i]==val) {
//              for(int j=i;j<nums.length-1;j++) {
//                  nums[j]=nums[j+1];
//              }
//              i--;
//          }
//      }
//        return nums.length-count;
//    }
    
}


```


# Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
```
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

- My Answer 

呃，算作弊了？

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月10日
 */
public class ImplementstrStr
{

    public static void main(String[] args)
    {
        String haystack="hello",needle="ll";
        System.out.println(strStr(haystack, needle));
    }

    
    public static int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}


```

# Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
```
Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0
```

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月10日
 */
public class SearchInsertPosition
{

    public static void main(String[] args)
    {
        int[] nums= {1,3,5,6};
        int target=0;
        System.out.println(searchInsert(nums, target));

    }
    
    public static int searchInsert(int[] nums, int target) {
        for(int i=0;i<nums.length;i++) {
            if(nums[i]>=target)
                return i;
        }
        return nums.length;
    }

}
```

# Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221


1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
```
Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
```

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月12日
 */
public class CountandSay
{
    public static void main(String[] args)
    {
        System.out.println(countAndSay(7));
    }
    
    //The description of the problem is a little confusing, may taking some time to understand, but shortly, just a "count number" game~
    public static String countAndSay(int n) {
        if(n==1)
            return "1";
        if(n==2)
            return "11";
        
        char[] lastStr=countAndSay(n-1).toCharArray();
        String result="";
        int count=1;
        for(int i=0;i<lastStr.length-1;i++) {
                if(lastStr[i+1]==lastStr[i]) {
                    count++;
                    if(i==lastStr.length-2) {
                        result+=count+""+lastStr[i];
                    }
                }
                else {
                    result+=count+""+lastStr[i];
                    count=1;
                    if(i==lastStr.length-2) {
                        result+="1"+lastStr[i+1];
                    }
                }
        }
        
        return result;
    }
}


```

# Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月12日
 */
public class MaximumSubarray
{
  public static void main(String[] args)
  {
     int nums[]={-2,1,-3,4,-1,2,1,-5,4};
     System.out.println(maxSubArray(nums));
  }
  
  /**
   *  for any sum tempSum over several items, the criteria that it bases on to decide whether or not to add next item c is that:
   *    if tempSum<0, then adding c will only makes sum fewer, so we replace tempSum's value with c;
   *    else, then add c and see whether tempSum>sum:
   *        if tempSum>sum, replace sum with tempSum;
   *        else, do nothing;
   * @param nums
   * @return
   */
  
  public static int maxSubArray(int[] nums) {
      if(nums.length==0)
          return 0;
      int tempSum=nums[0];
      int sum=tempSum;
      for(int i=1;i<nums.length;i++) {
          if(tempSum<0) {
              tempSum=nums[i];
          }
          else {
              tempSum+=nums[i];
          }
          
          if(tempSum>sum)
              sum=tempSum;
          
      }
      return sum;
  }
}


```


# Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
```
Input: "Hello World"
Output: 5
```


- My Answer

```
package easy;

import java.util.regex.Pattern;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月12日
 */
public class LengthofLastWord
{

    public static void main(String[] args)
    {
        System.out.println(lengthOfLastWord("asd asd"));

    }
    
    public static int lengthOfLastWord(String s) {
        if(s.equals(""))
            return 0;
        
        if(s.contains(" ")) {

            String[] strs=s.split(" ");
            
            // only consists of " ", then strs.length=0
            if(strs.length==0)
                return 0;
            else
                return strs[strs.length-1].length();
            
        }
        
        else 
            return s.length();
    }
}
```

# Plus One

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

- My Answer

```
package easy;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月12日
 */
public class PlusOne
{
    static int index=0;

    public static void main(String[] args)
    {
        int[] digits= {9,9,9,9,9,9,9,9,9,9,9,9,9};
        int nums[]=plusOne(digits);
        for(int i=0;i<nums.length;i++) {
            System.out.print(nums[i]+" ");
        }

    }
    
    public static int[] plusOne(int[] digits) {
        int len=digits.length;
        int count=0;
        for(int i=0;i<digits.length;i++) {
            if(digits[len-i-1]+1==10) {
                count++;
            }
            else
                break;
        }
        int nums[];
        if(count==len) {
            nums=new int[count+1];
            nums[0]=1;
            for(int i=1;i<nums.length;i++)
                nums[i]=0;
        }else{
            nums=new int[len];
            for(int i=0;i<nums.length;i++) {
                if(i<count)
                    nums[len-i-1]=0;
                else {
                    nums[len-i-1]=digits[len-i-1];
                    if(i==0 || i==count)
                        nums[len-i-1]+=1;
                }
            }
        }
        
        return nums;
    }
    
    //  This answer doesn't work when input is greater than Integer.MAX_VALUE;
//  public static int[] plusOne(int[] digits) {
//      int count=1;
//      int sum=digits[0];
//      for(int i=1;i<digits.length;i++) {
//          sum*=10;
//          sum+=digits[i];
//      }
//      sum+=1;
//      List<Integer> list=new ArrayList<Integer>();
//      while(sum/10!=0) {
//          int yushu=sum%10;
//          list.add(yushu);
//          sum/=10;
//      }
//      list.add(sum);
//      int nums[]=new int[list.size()];
//      for(int i=0;i<nums.length;i++)
//          nums[i]=list.get(nums.length-i-1);
//        return nums;
//    }

}

```


# Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

- My Answer

```
package easy;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月12日
 */
public class AddBinary
{

    public static void main(String[] args)
    {
        System.out.println("----------");
        System.out.println(addBinary("101111", "10"));

    }
    
    public static String addBinary(String a, String b) {
        List<Character> list=new ArrayList<Character>();
        
        char[] arrA,arrB;
        
        char[] tempA=a.toCharArray(),tempB=b.toCharArray();
        int len=Math.max(tempA.length, tempB.length);
        if(len==tempA.length) {
            arrA=tempA;
            arrB=new char[len];
            for(int i=0;i<len;i++) {
                if(i<tempB.length) {
                    arrB[len-i-1]=tempB[tempB.length-i-1];
                }else
                    arrB[len-i-1]='0';
            }
        }
        else {
            arrB=tempB;
            arrA=new char[len];
            for(int i=0;i<len;i++) {
                if(i<tempA.length) {
                    arrA[len-i-1]=tempA[tempA.length-i-1];
                }else
                    arrA[len-i-1]='0';
            }
        }
        
        boolean jinwei=false;
        
        for(int i=len-1;i>=0;i--) {
            if(arrA[i]=='1' && arrB[i]=='1' && jinwei==true) {
                list.add('1');
                jinwei=true;
            }
            else if(arrA[i]=='1' && arrB[i]=='1' && jinwei==false) {
                list.add('0');
                jinwei=true;
            }
            else if((arrA[i]=='1' || arrB[i]=='1') && jinwei==true) {
                list.add('0');
                jinwei=true;
            }
            else if((arrA[i]=='1' || arrB[i]=='1') && jinwei==false) {
                list.add('1');
            }
            else if((arrA[i]=='0' && arrB[i]=='0') && jinwei==true) {
                list.add('1');
                jinwei=false;
            }
            else{
                list.add('0');
            }
        }

        char[] result;
        
        if(jinwei==false) {
            result=new char[len];
            for(int i=0;i<len;i++)
                result[len-i-1]=list.get(i);
        }else {
            result=new char[len+1];
            for(int i=0;i<len;i++)
                result[len-i]=list.get(i);
            result[0]='1';
        }
        
        return new String(result);
    }
}


```

# Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

```
Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
```

- My Answer
```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月13日
 */
public class SqrtX
{

    public static void main(String[] args)
    {
        //2147395600
        System.out.println(Integer.MAX_VALUE);
        System.out.println(mySqrt(Integer.MAX_VALUE));
        System.out.println(46341*46341);

    }
    
    public static int mySqrt(int x) {
        int delta=Integer.MAX_VALUE;
        int result=0;
        for(int i=0;i<=x;i++) {
            if(i*i>x)
                break;
            // avoid overflow
            if(i*i<0) {
                result=i-1;
                break;
            }
            if(x-i*i<delta) {
                delta=x-i*i;
                result=i;
            }
        }
        return result;
    }

}


```

# Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

```
Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```


- My Answer

```
package easy;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月13日
 */
public class ClimbingStairs
{

    public static void main(String[] args)
    {
        System.out.println(climbStairs(44));
    }
    
    // using normal iteration way to do this. Compared with recursive way, this simplifies the calculation process, so it's much faster!
    // "Simplify" means many duplicated calculations are avoided.
    public static int climbStairs(int n) {
        if(n==1)
            return 1;
        if(n==2)
            return 2;
        
        List<Integer> list=new ArrayList<Integer>();
        
        list.add(0);
        list.add(1);
        list.add(2);
        
        for(int i=3;i<n;i++) {
            list.add(list.get(i-1)+list.get(i-2));
        }
        
        return list.get(n-1)+list.get(n-2);
    }

    /**
     * classical recursive problem, just think:
     *   When you're going to finish climbing n stairs, you can only choose to climb either 1 step or 2 steps as last action, then
     *   it means there are total  #(climbStairs(n-1)) plus #(climbStairs(n-2)) cases where you can finish climbing n stairs.
     *   Then achieve in recursive way!
     *   
     *  However, this simple recursive method would exceeds time limit on leetcode for input 44!!!!
     * @param n
     * @return
     */
    
//  public static int climbStairs(int n) {
//      if(n==1)
//          return 1;
//      if(n==2)
//          return 2;
//      return climbStairs(n-1)+climbStairs(n-2);
//    }
}

```

# Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

```
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
```

- My Answer
```
package easy;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月13日
 */
public class RemoveDuplicatesfromSortedList
{

    public static void main(String[] args)
    {
        ListNode node1=new ListNode(1);
        ListNode node2=new ListNode(1);
        ListNode node3=new ListNode(2);
        ListNode node4=new ListNode(3);
        ListNode node5=new ListNode(3);
        node1.next=node2;node2.next=node3;node3.next=node4;node4.next=node5;
        ListNode head=deleteDuplicates(node1);
        while(head!=null) {
            System.out.println(head.val);
            head=head.next;
        }
        
    }
    
    public static ListNode deleteDuplicates(ListNode head) {
        Set<Integer> set=new HashSet<Integer>();
        
        ListNode lastNode=head,resultHead=head;
        while(head!=null) {
            if(set.contains(head.val)) {
                lastNode.next=head.next;
                head.next=null;
                head=lastNode.next;
            }else {
                set.add(head.val);
                lastNode=head;
                head=head.next;
            }
        }
        return resultHead;
    }
}
```

# Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

- My Answer
```


/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月13日
 */
public class MergeSortedArray
{

    public static void main(String[] args)
    {
        //-5 2 3 100 1000
        int m=2,n=3;
        int[] nums1=new int[m+n];
        nums1[0]=3;nums1[1]=100;
        int[] nums2=new int[n];
        nums2[0]=-5;nums2[1]=2;nums2[2]=1000;
        merge(nums1, m, nums2, n);
        for(int i=0;i<nums1.length;i++)
            System.out.println(nums1[i]+" ");
        
    }
    
    
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int index1=0,index2=0;
        int[] tempArr=new int[m+n];
            while(index1<m && index2<n) {
                if(nums2[index2]>=nums1[index1]) {
                    tempArr[index1+index2]=nums1[index1];
                    index1++;
                }else {
                    tempArr[index1+index2]=nums2[index2];
                    index2++;
                }
            }
            
            if(index1<m) {
                for(;index1<m;index1++)
                    tempArr[index1+index2]=nums1[index1];
            }
            else {
                for(;index2<n;index2++)
                    tempArr[index1+index2]=nums2[index2];
            }
            
            for(int i=0;i<tempArr.length;i++)
                nums1[i]=tempArr[i];
    }

}


```

# Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

```
Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```


- My Answer

```
package easy;

/**
 *  @author Tom Qian
 *  @email tomqianmaple@outlook.com
 *  @github https://github.com/bluemapleman
 *  @date 2018年1月13日
 */
 

public class SameTree
{

    public static void main(String[] args)
    {
        TreeNode p=new TreeNode(1);
        TreeNode node2=new TreeNode(2);
        p.left=node2;
        TreeNode q=new TreeNode(1);
        TreeNode node4=new TreeNode(2);
        q.right=node4;
        System.out.println(isSameTree(p, q));

    }
    
    // Classical Recursive Method
    public static boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null) {
            return true;
        }
        else if(p!=null && q!=null){
            if(p.val==q.val)
                return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
            else
                return false;
        }
        else
            return false;
    }
    
    
}

//Definition for a binary tree node.
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode(int x) { val = x; }
}

```


# Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

```
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
```

Note:
Bonus points if you could solve it both recursively and iteratively.

- My Answer
```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月16日
 */
public class SymmetricTree
{

    public static void main(String[] args)
    {
//      TreeNode root=new TreeNode(1);
//      TreeNode left1=new TreeNode(2),left2=new TreeNode(3),left3=new TreeNode(4);
//      root.left=left1;left1.left=left2;left1.right=left3;
//      TreeNode right1=new TreeNode(2),right2=new TreeNode(3),right3=new TreeNode(4);
//      root.right=right1;right1.left=right3;right1.right=right2;
//      System.out.println(isSymmetric(root));
        
//      TreeNode root=new TreeNode(1);
//      TreeNode left1=new TreeNode(2),left2=new TreeNode(3);
//      root.left=left1;left1.right=left2;
//      TreeNode right1=new TreeNode(2),right2=new TreeNode(3);
//      root.right=right1;right1.right=right2;
//      System.out.println(isSymmetric(root));
        
        TreeNode root=new TreeNode(1);
        TreeNode left1=new TreeNode(2);
        root.left=left1;
        TreeNode right1=new TreeNode(3);
        root.right=right1;
        System.out.println(isSymmetric(root));
    }
    
    public static boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }
    
    public static boolean isMirror(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null || t2 == null) return false;
        return (t1.val == t2.val)
            && isMirror(t1.right, t2.left)
            && isMirror(t1.left, t2.right);
    }
    
    // My Thought: First, get the mirror of given tree, and judge whether the mirror is the same as the given tree.
    // But I don't know how to replicate trees, so my realization is not complete, just put part of my codes here as a reference... 
//  public static boolean isSymmetric(TreeNode root) {
//      TreeNode mirrorRootNode=getMirrorTree(root);
//      System.out.println(root.left.val);
//      System.out.println(mirrorRootNode.left.val);
//      return judgeSameTree(root, mirrorRootNode);
//    }
//  
//  public static TreeNode getMirrorTree(TreeNode root) {
//      if(root==null)
//          return null;
//      TreeNode temp=root.left;
//      root.left=root.right;
//      root.right=temp;
//      getMirrorTree(root.left);
//      getMirrorTree(root.right);
//      return root;
//  }
//  
//  public static boolean judgeSameTree(TreeNode root1,TreeNode root2) {
//      if(root1==null && root2==null)
//          return true;
//      if(root1==null || root2==null)
//          return false;
//      if(root1.val==root2.val) {
//          return true && judgeSameTree(root1.left, root2.left) && judgeSameTree(root1.right, root2.right);
//      }else {
//          return false;
//      }
//  }

}


```

# Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月17日
 */
public class MaximumDepthofBinaryTree
{

    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(1);
        TreeNode left1=new TreeNode(2),left2=new TreeNode(3),right1=new TreeNode(4);
        root.left=left1;left1.right=left2;root.right=right1;
        System.out.println(maxDepth(root));
    }
    
    public static int maxDepth(TreeNode root) {
        if(root==null)
            return 0;
        else
                return 1+Math.max(maxDepth(root.left),maxDepth(root.right));
    }

}

```

# Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```

- My Answer

```
package easy;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.concurrent.ArrayBlockingQueue;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月17日
 */
public class BinaryTreeLevelOrderTraversalII
{

    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(3);
        TreeNode left1=new TreeNode(9);
        root.left=left1;
        TreeNode right1=new TreeNode(20),right2=new TreeNode(15),right3=new TreeNode(7);
        root.right=right1;right1.left=right2;right1.right=right3;
        for(List<Integer> list:levelOrderBottom(root)) {
            for(Integer ele:list) {
                System.out.print(ele+",");
            }
            System.out.println();
        }
    }
    
    // Make use of Stack's feature: FILO
    
    public static List<List<Integer>> levelOrderBottom(TreeNode root) {
        if(root==null)
            return new ArrayList<List<Integer>>();
        
        ArrayDeque<List<Integer>> bigQueue=new ArrayDeque<List<Integer>>();  
        List<Integer> list=new ArrayList<Integer>();
        
        
        ArrayDeque<TreeNode> nodeQueue=new ArrayDeque<TreeNode>();
        nodeQueue.push(root);
        
        ArrayDeque<TreeNode> tempQueue=new ArrayDeque<TreeNode>();
        while(!nodeQueue.isEmpty()) {
            list=new ArrayList<Integer>();
            while(!nodeQueue.isEmpty()) {
                TreeNode node=nodeQueue.poll();
//              System.out.println(node.val);
                if(node.left!=null)
                    tempQueue.add(node.left);
                if(node.right!=null)
                    tempQueue.add(node.right);
                list.add(node.val);
            }
            
            bigQueue.push(list);
            
            while(!tempQueue.isEmpty()) {
                nodeQueue.add(tempQueue.poll());
            }
        }
        
        List<List<Integer>> bigList=new ArrayList<List<Integer>>();
        while(!bigQueue.isEmpty()){
            bigList.add(bigQueue.pop());
        }
        
        return bigList;
    }

}


```

# Convert Sorted Array to Binary Search Tree


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
```
      0
     / \
   -3   9
   /   /
 -10  5
```

- My Answer

```
package easy;

import java.util.Arrays;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月17日
 */
public class ConvertSortedArraytoBinarySearchTree
{

    public static void main(String[] args)
    {
        int[] nums={-10,-3,0,5,9};
        TreeNode root=sortedArrayToBST(nums);
        System.out.println(root.val);
        System.out.println(root.left.val);
        System.out.println(root.right.val);
        System.out.println(root.left.left.val);
        System.out.println(root.right.left.val);
    }

    // Recursive way
    public static TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length==0)
            return null;
        if(nums.length==1)
            return new TreeNode(nums[0]);
        int len=nums.length;
        
        int middle=len/2;
        
        TreeNode root=new TreeNode(nums[middle]);
        
        int[] leftNums=Arrays.copyOfRange(nums, 0, middle);
        int[] rightNums=Arrays.copyOfRange(nums, middle+1, len);
        
        root.left=sortedArrayToBST(leftNums);
        root.right=sortedArrayToBST(rightNums);
        
        return root;
    }

}


```


# Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月17日
 */
public class BalancedBinaryTree
{
    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(1);
        TreeNode left1=new TreeNode(2),left2=new TreeNode(3);
        root.left=left1;left1.left=left2;
        System.out.println(isBalanced(root));
    }
    
    public static boolean isBalanced(TreeNode root) {
        if(root==null)
            return true;
        else {
            if(Math.abs(getMaxTreeDepth(root.left)-getMaxTreeDepth(root.right))<=1){
                return isBalanced(root.left) && isBalanced(root.right);
            }else {
                return false;
            }
        }
    }
    
    public static int getMaxTreeDepth(TreeNode root) {
        if(root==null)
            return 0;
        else
            return 1+Math.max(getMaxTreeDepth(root.left),getMaxTreeDepth(root.right));
    }
}


```

#  Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月17日
 */
public class MinimumDepthofBinaryTree
{
    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(1);
        TreeNode left1=new TreeNode(2),left2=new TreeNode(4),left3=new TreeNode(5);
        root.left=left1;left1.left=left2;left2.right=left3;
        TreeNode right1=new TreeNode(3);
        root.right=right1;
        System.out.println(minDepth(root));
    }
    
    public static int minDepth(TreeNode root) {
        if(root==null)
                return 0;
        else if(root.left==null && root.right==null)
                return 1;
        else if(root.left!=null && root.right!=null)
                return 1+Math.min(minDepth(root.left), minDepth(root.right));
        else
                if(root.left!=null)
                    return 1+minDepth(root.left);
                else
                    return 1+minDepth(root.right);
    }
}


```


# Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

- My Answer

```
package easy;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月18日
 */
public class PascalsTriangle
{
    public static void main(String[] args)
    {
        for(List<Integer> list:generate(20)) {
            for(Integer ele:list)
                System.out.print(" "+ele);
            System.out.println();
        }
    }
    
    // Permutation Problem 
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> bigList=new ArrayList<List<Integer>>();
        if(numRows==0)
            return bigList;
        
        for(int i=0;i<numRows;i++) {
            List<Integer> list=new ArrayList<Integer>();
            for(int j=0;j<=i;j++) {
                list.add(getCombinationNumber(i, j));
            }
            bigList.add(list);
        }
        return bigList;
    }
    
    public static int getCombinationNumber(int m,int n) {
        if(n==0)
            return 1;
        // Using the property of combination theory to simplify calculation
        if(n>m/2)
            n=m-n;
        
        long nFactorial=1l;
        for(int i=1;i<n;i++)
            nFactorial*=(i+1);
        
        long mFactorial=1;
        for(int i=0;i<n;i++)
            mFactorial*=(m-i);
        
        return (int)(mFactorial/nFactorial);
        
        
    }
}


```


# Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

- My Answer

```
package easy;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月18日
 */
public class PascalsTriangleII
{
    public static void main(String[] args)
    {
        System.out.println(Long.MAX_VALUE);
        System.out.println(getCombinationNumber(30, 13));
        System.out.println(getCombinationNumber(30, 14));
        System.out.println(getCombinationNumber(30, 15));
//      for(Integer ele:getRow(3)) {
//          System.out.println(ele+" ");
//      }
    }
    
    public static List<Integer> getRow(int rowIndex) {
        List<Integer> list=new ArrayList<Integer>();
        for(int i=0;i<=rowIndex;i++) {
                list.add(getCombinationNumber(rowIndex,i));
        }
        return list;
    }
    
    public static int getCombinationNumber(int m,int n) {
        if(n==0)
            return 1;
        // Using the property of combination theory to simplify calculation
        if(n>m/2)
            n=m-n;
        
        List<Integer> nList=new ArrayList<Integer>(),mList=new ArrayList<Integer>(); 
        
        for(int i=0;i<n;i++) {
            int nFactor=i+1;
            int mFactor=m-i;
            nList.add(nFactor);
            mList.add(mFactor);
        }
        
        for(int i=0;i<nList.size();i++) {
            for(int j=0;j<mList.size();j++) {
                int nFactor=nList.get(i);
                int mFactor=mList.get(j);
                if(mFactor%nFactor==0) {
                    mList.set(j, mFactor/nFactor);
                    nList.set(i,1);
                    break;
                }
            }
        }
        long mFactorial=1l,nFactorial=1l;
        for(int i=0;i<nList.size();i++) {
            nFactorial*=nList.get(i);
        }
        
        for(int j=0;j<mList.size();j++) {
            mFactorial*=mList.get(j);
        }
        
        
        return (int)(mFactorial/nFactorial);
        
        
    }
}
```

# Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
```

Example 2:
```
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
```

- My Answer
```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月20日
 */
public class BestTimetoBuyandSellStock
{

    public static void main(String[] args)
    {
        int[] prices= {7, 1, 5, 3, 6, 4};
        System.out.println(maxProfit(prices));
    }
    
    public static int maxProfit(int[] prices) {
        // First, jump over region showing descending trend
        int start=0;
        for(int i=0;i<prices.length-1;i++) {
            if(prices[i]<prices[i+1]) {
                start=i;
                break;
            }
            start++;
        }
        
        int max=Integer.MIN_VALUE;
        for(int i=start;i<prices.length-1;i++) {
            int buy=prices[i];
            for(int j=i+1;j<prices.length;j++) {
                int sell=prices[j];
                if(buy<sell) {
                    int delta=sell-buy;
                    if(delta>max)
                        max=delta;
                }
            }
        }
        if(max==Integer.MIN_VALUE)
            max=0;
        return max;
    }
}
```

# Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

- My Answer

```
package easy;

import java.util.Arrays;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月20日
 */
public class BestTimetoBuyandSellStockII
{
    public static void main(String[] args)
    {
        int[] prices= {5,2,3,2,6,6,2,9,1,0,7,4,5,0};//{3,2,6,5,0,3};//{3,3,5,0,0,3,1,4};//{9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8};
        System.out.println(maxProfit(prices));
    }
    
    public static int maxProfit(int[] prices) {
        int start=getAscendingStart(prices, 0);
        int max=Integer.MIN_VALUE;
        int sumProfit=0;
        int heapIndex=0;
        heapIndex=getHeapIndex(prices, start);
        while((heapIndex=getHeapIndex(prices, start))<prices.length) {
            sumProfit+=prices[heapIndex]-prices[start];
            start=getAscendingStart(prices, heapIndex+1);
        }
        
        if(sumProfit>max)
            max=sumProfit;
        
        return max;
         
    }
    
    
    public static int getAscendingStart(int[] prices,int start) {
        int ascendingStart=start;
        
        for(;ascendingStart<prices.length-1;ascendingStart++) {
            if(prices[ascendingStart]<prices[ascendingStart+1])
                break;
        }
        
        return ascendingStart;
    }
    
    public static int getHeapIndex(int prices[],int start) {
        for(;start<prices.length-2;start++) {
            if(prices[start]<=prices[start+1] && prices[start+1]>prices[start+2]) {
                break;
            }
        }
        return start+1;
    }
}


```

# Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
```
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
```

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

- My Answer

```
package easy;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月20日
 */
public class ValidPalindrome
{
    public static void main(String[] args)
    {
        System.out.println(isPalindrome("0P"));
    }
    
    public static boolean isPalindrome(String s) {
        if(s.equals("") || s.length()==1)
            return true;
        s=s.replaceAll(" ","");
        s=s.replaceAll(",","");
        s=s.replaceAll("\n","");
        s=s.replaceAll("\r","");
        
        // remove non-alphanumeric characters
        String regex="[a-zA-Z0-9]+";
        Pattern pattern=Pattern.compile(regex);
        Matcher matcher=pattern.matcher(s);
        String goalStr="";
        while(matcher.find()) {
            goalStr+=matcher.group();
        }
        s=goalStr.toLowerCase();
        
        int len=s.length();
        for(int i=0;i<len/2;i++) {
            if(s.charAt(i)==s.charAt(len-i-1))
                continue;
            else
                return false;
        }
        
        return true;
    }
}
```

# Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月21日
 */
public class PathSum
{
    public static void main(String[] args)
    {
        TreeNode root=new TreeNode(5);
        TreeNode left1=new TreeNode(4),left2=new TreeNode(11),left3=new TreeNode(7),left4=new TreeNode(2);
        root.left=left1;left1.left=left2;left2.left=left3;left2.right=left4;
        TreeNode right1=new TreeNode(8),right2=new TreeNode(13),right3=new TreeNode(4),right4=new TreeNode(1);
        root.right=right1;right1.left=right2;right1.right=right3;right3.left=right4;
        System.out.println(hasPathSum(root,26));
        
    }
    
    // Layerwise decreasing goal value, and tried finding goal value in sub tree recursively
    public static boolean hasPathSum(TreeNode root, int sum) {
        if(root==null)
            return false;
        
        if(root.val==sum && root.left==null && root.right==null)
            return true;
        
        
        int goal=sum-root.val;
        return hasPathSum(root.left, goal) || hasPathSum(root.right, goal);
    }
}
```

# Single Number

Given an array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

- My Answer

```
class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> map=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++)
            if(map.containsKey(nums[i]))
                map.put(nums[i],map.get(nums[i])+1);
            else
                map.put(nums[i],1);
                
        Set<Integer> keys=map.keySet();
        for(Integer key:keys)
            if(map.get(key)==1)
                return key;
        
        return -1;
    }
}
```

# Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:

Can you solve it without using extra space?

- My Answer
```
package easy;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月21日
 */
public class LinkedListCycle
{
    public static void main(String[] args)
    {
        ListNode head=new ListNode(1);
        ListNode node1=new ListNode(1);ListNode node2=new ListNode(1);
        head.next=node1;node1.next=node2;node2.next=null;
        System.out.println(hasCycle(head));
        
    }
    
     public static boolean hasCycle(ListNode head) {
        Set<ListNode> set=new HashSet<ListNode>();
        while(head!=null) {
            if(!set.contains(head)) {
                set.add(head);
            }else {
                return true;
            }
            head=head.next;
        }
        return false;
     }
}


```

# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

- My Answer
```
package easy;

import java.util.ArrayDeque;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月21日
 */
public class MinStack
{
    private ArrayDeque<Integer> stack;
    public static void main(String[] args)
    {
         MinStack obj = new MinStack();
         obj.push(-3);
         obj.push(-2);
         obj.push(10);
         obj.pop();
         obj.pop();
         int param_3 = obj.top();
         int param_4 = obj.getMin();
         System.out.println("p3:"+param_3+",p4:"+param_4);
    }
    
    /** initialize your data structure here. */
    public MinStack() {
            stack=new ArrayDeque<Integer>();
    }
    
    public void push(int x) {
        stack.push(x);
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
            ArrayDeque<Integer> tempStack=new ArrayDeque<Integer>();
            int min=Integer.MAX_VALUE;
            int size=stack.size();
            
        for(int i=0;i<size;i++) {
                int ele=stack.pop();
                stack.add(ele);
                if(ele<min)
                    min=ele;
        }
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

# Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
```

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

- My Answer

```
package easy;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月21日
 */
public class IntersectionofTwoLinkedLists
{
    public static void main(String[] args)
    {
//      ListNode list1Head=new ListNode(1);
//      ListNode list1node1=new ListNode(2);
//      list1Head.next=list1node1;
//      ListNode list2Head=new ListNode(1);
//      ListNode intersection=new ListNode(3);
//      list1node1.next=intersection;
//      list2Head.next=intersection;
//      ListNode intersectionNext=new ListNode(4);
//      intersection.next=intersectionNext;
        
        ListNode node1=new ListNode(2);ListNode node2=new ListNode(3);
        node1.next=node2;
        ListNode node3=node2;
        System.out.println(getIntersectionNode(node1,node3).val);
    }
    
    public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> set=new HashSet<ListNode>();
        while(headA!=null && headB!=null) {
            if(set.contains(headA))
                return headA;
            set.add(headA);
            headA=headA.next;
            
            if(set.contains(headB))
                return headB;
            set.add(headB);
            headB=headB.next;
        }
        
        while(headA!=null) {
            if(set.contains(headA))
                return headA;
            set.add(headA);
            headA=headA.next;
        }
        
        while(headB!=null) {
            if(set.contains(headB))
                return headB;
            set.add(headB);
            headB=headB.next;
        }
            
        return null;
    }
}


```

# Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.
```
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
```

- My Answer

```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月23日
 */
public class TwoSumII
{
    public static void main(String[] args)
    {
        int[] numbers= {2,7,11,15};
        int target=9;
        int[] two=twoSum(numbers, target);
        System.out.println(two[0]);
        System.out.println(two[1]);
    }
    
    public static int[] twoSum(int[] numbers, int target) {
        int[] two=new int[2];
        for(int i=0;i<numbers.length;i++) {
                int first=numbers[i];
                for(int j=i+1;j<numbers.length;j++) {
                    int second=numbers[j];
                    if(first+second==target) {
                        two[0]=i+1;
                        two[1]=j+1;
                        return two;
                    }
                }
        }
        return two;
    }
}


```

# Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
```

- My Answer

这一题暂时不会做，求大神解答！

大概已有思路知道是用“除n取余法”，把这个当成生成26进制的数的字符表示问题来做，但是在边界地方的表示总会弄错，暂时想不通。


# Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

- My Answer

```
package easy;

import java.util.HashMap;
import java.util.Map;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月23日
 */
public class MajorityElement
{
    public static void main(String[] args)
    {
        int nums[]= {1,2,3,4,5,6,1,-1,0,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3};
        System.out.println("len:"+nums.length);
        System.out.println(majorityElement(nums));
    }

    public static int majorityElement(int[] nums) {
        Map<Integer,Integer> map=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++) {
            int key=nums[i];
            if(map.containsKey(key)) {
                map.put(key, map.get(key)+1);
            }else {
                map.put(key, 1);
            }
            if(map.get(key)>nums.length/2)
                return key;
        }
        return -1;
    }
}


```


# Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
```

(和上上一题互为镜像题。)

- My Answer
```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月23日
 */
public class ExcelSheetColumnNumber
{
    public static void main(String[] args)
    {
        
    }
    
    public static int titleToNumber(String s) {
        int sum=0;
        for(int i=0;i<s.length();i++) {
            int delta=s.charAt(i)-'@';
            for(int j=i+1;j<s.length();j++)
                delta*=26;
            sum+=delta;
        }
        return sum;
    }
}
```

# Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

- My Answer
```
package easy1;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月23日
 */
public class FactorialTrailingZeroes
{
    // #(2-5 pair) and #(n*10)
    public static void main(String[] args)
    {
        System.out.println(1/5);
        for(int i=1;i<30;i++)
            System.out.println(i+"!:"+getFactorial(i)+" "+trailingZeroes(i));
    }
    
    //count the number of 5 is all we need to do!
    //But attention: We need to focus on numbers that are 5^n, so we iteratively let n be divided by 5, and add quotient up.
    public static int trailingZeroes(int n) {
        if(n==0)
            return 0;
        
        int nums=0;
        while(n/5!=0) {
            nums+=n/5;
            n/=5;
        }
        return nums;
    }
    
    public static long getFactorial(int n) {
        if(n==1)
            return n*1;
        return n*(getFactorial(n-1));
    }
    
}
```

# Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:

Could you do it in-place with O(1) extra space?

Related problem: Reverse Words in a String II

- My Answer
```
package easy;

import java.util.Arrays;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月24日
 */
public class RotateArray
{
    public static void main(String[] args)
    {
        int[] nums= {1,2,3,4,5,6,7,8};
        rotate(nums, 11);
        for(int i=0;i<nums.length;i++)
            System.out.println(nums[i]+" ");
    }
    
    public static void rotate(int[] nums, int k) {
        if(k<nums.length) {
                int[] rotatePart=Arrays.copyOfRange(nums, nums.length-k, nums.length);
                for(int i=0;i<nums.length-k;i++) 
                    nums[nums.length-i-1]=nums[nums.length-k-i-1];
                for(int i=0;i<rotatePart.length;i++)
                    nums[i]=rotatePart[i];
        }else {
                k=k%nums.length;
                rotate(nums,k);
        }
    }
}


```

# Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:

If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

- My Answer
```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月24日
 */
public class ReverseBits
{
    public static void main(String[] args)
    {
        System.out.println("result:"+reverseBits(43261596));
    }
    
    // you need treat n as an unsigned value
    public static int reverseBits(int n) {
            StringBuilder binStr=new StringBuilder(Integer.toBinaryString(n));
            int digitDelta=32-binStr.length();
            while(digitDelta-->0)
                binStr.insert(0, "0");
        binStr=binStr.reverse();
        return Integer.parseUnsignedInt(binStr.toString(),2);
    }
}

```

# Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.


- My Answer
```
package easy;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月24日
 */
public class Numberof1Bits
{
    public static void main(String[] args)
    {
        System.out.println(hammingWeight(11));
    }
    
    // you need to treat n as an unsigned value
    public static int hammingWeight(int n) {
            StringBuilder binStr=new StringBuilder(Integer.toUnsignedString(n,2));
            int digitDelta=32-binStr.length();
//          while(digitDelta-->0)
//              binStr.insert(0,"0");
            int count=0;
            for(int i=0;i<binStr.length();i++)
                if(binStr.charAt(i)=='1')
                    count++;
        return count;
    }
}
```

# House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

- My Answer

```
package easy1;

import java.util.Arrays;

import com.mysql.fabric.xmlrpc.base.Array;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月24日
 */
public class HouseRobber
{
    public static void main(String[] args)
    {
        int[] nums= {1,2,3,4,5,6};
        System.out.println(rob(nums));
    }
    
    // When adding n+1 house(number) to street(array) with #(n) houses(numbers), we only need to consider two cases:
    // 1: combine all possible houses' money with new house's money;
    // 2: combine all possible houses' money without new house;
    
    // Forward Iteration instead of Rcursion can effectively reduce time cose. (Dynamic Programming v.s. Recursive Method)
    public static int rob(int[] nums) {
        int len=nums.length;
        int[] solutions=new int[len];
        switch(len) {
            case 0:return 0;
            case 1:return nums[0];
            case 2:return Math.max(nums[0], nums[1]);
            case 3:return Math.max(nums[1],nums[0]+nums[2]);
            default:solutions[0]=nums[0];solutions[1]=Math.max(nums[0], nums[1]);solutions[2]=Math.max(nums[1],nums[0]+nums[2]);
        }
        for(int i=3;i<len;i++) {
            solutions[i]=Math.max(solutions[i-1], solutions[i-2]+nums[i]);
        }
        return solutions[len-1];
    }
}
```

# Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
$$1^2 + 9^2 = 82$$
$$8^2 + 2^2 = 68$$
$$6^2 + 8^2 = 100$$
$$1^2 + 0^2 + 0^2 = 1$$

- My Answer
```
package easy;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月24日
 */
public class HappyNumber
{
    public static void main(String[] args)
    {
        System.out.println(isHappy(2));
    }
    
    public static boolean isHappy(int n) {
        Set<Integer> set=new HashSet<Integer>();
        int sum=0;
        while(sum!=1) {
            sum=0;
            while(n/10!=0 || n>0) {
                int digit=n%10;
                sum+=digit*digit;
                n/=10;
            }
            
            if(sum==1)
                return true;
            else
                n=sum;
            
            if(set.contains(sum))
                return false;
            else
                set.add(sum);
        }
        return false;
        }
    
}
```

# Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

- My Answer
```
package easy1;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class RemoveLinkedListElements
{
    public static void main(String[] args)
    {
        ListNode head=new ListNode(1);
        ListNode node1=new ListNode(2),node2=new ListNode(6),node3=new ListNode(4),node4=new ListNode(6);
        head.next=node1;node1.next=node2;node2.next=node3;node3.next=node4;
        ListNode node=removeElements(head, 6);
        while(node!=null) {
            System.out.print(node.val+" ");
            node=node.next;
        }
    }
    
    public static ListNode removeElements(ListNode head, int val) {
        if(head==null)
            return head;
        ListNode stayHead=head;
        ListNode lastNode=null;
        while(head!=null) {
            if(head.val==val) {
                //If head node's value is equal to val, then directly assign head to next node
                if(lastNode==null) {
                    head=head.next;
                    stayHead=head;
                }else {
                    lastNode.next=head.next;
                    head.next=null;
                    head=lastNode.next;
                }
            }else {
                lastNode=head;
                head=head.next;
            }
        }
        return stayHead;
    }
}
```

#  Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.

- My Answer
```
package easy1;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class CountPrimes
{
    public static void main(String[] args)
    {
        System.out.println(countPrimes(499979));
    }
    
    // First of all, starting from 2, hypothesizing that all numbers are prime, then:
    //   Using [Prime Filtering Method] to pre-remove known composite:
    //   "If number i is a prime, then for any integer k>0, i*k must be a composite"
    //   Make use of above law, every time we find a new prime, we could pre-remove great amounts of composite and save time for judging prime. 
    public static int countPrimes(int n) {
        if(n==0 || n==1)
            return 0;
        boolean[] compositeArr=new boolean[n];
        List<Integer> primeList=new ArrayList<Integer>();
        for(int i=2;i<n;i++) {
            if(compositeArr[i]==true)
                continue;
            else {
                primeList.add(i);
                for(int k=2;i*k<n;k++)
                    compositeArr[i*k]=true;
            }
        }
        return primeList.size();
    }
}


```

# Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
```
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
```

Note:

You may assume both s and t have the same length.

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
public class IsomorphicStrings
{
    public static void main(String[] args)
    {
        System.out.println(isIsomorphic("ac", "ab"));
    }
    
    public static boolean isIsomorphic(String s, String t) {
        Map<Character,Character> map=new HashMap<Character,Character>();
        int len=s.length();
        for(int i=0;i<len;i++) {
            char schar=s.charAt(i);
            char tchar=t.charAt(i);
            if(map.containsKey(schar)) {
                // one character can map to at most 1 character 
                if(map.get(schar)==tchar)
                    continue;
                else
                    return false;
            }else {
                // no two character can map to the same character
                if(map.containsValue(tchar))
                    return false;
                map.put(schar,tchar);
            }
        }
        return true;
    }
}
```

# Reverse Linked List

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

- My Answer
```
package easy1;

import java.util.ArrayDeque;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class ReverseLinkedList
{
    public static void main(String[] args)
    {
        ListNode node1=new ListNode(1);
        ListNode node2=new ListNode(2);
        ListNode node3=new ListNode(3);
        node1.next=node2;
        node2.next=node3;
        ListNode head=reverseList(node1);
        while(head!=null) {
            System.out.print(head.val+" ");
            head=head.next;
        }
    }
    
    public static ListNode reverseList(ListNode head) {
        if(head==null)
            return head;
        
        ArrayDeque<ListNode> stack=new ArrayDeque<ListNode>();
        while(head!=null) {
            stack.push(head);
            head=head.next;
        }
        
        ListNode lastNode=stack.pop();
        ListNode reverseHead=lastNode;
        while(!stack.isEmpty()) {
            ListNode node=stack.pop();
            lastNode.next=node;
            node.next=null;
            lastNode=node;
        }
        return reverseHead;
    }
}

```

# Contains Duplicate

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

- My Answer
```
package easy1;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Tom Qian
 * @email tomqianmaple@outlook.com
 * @github https://github.com/bluemapleman
 * @date 2018年1月25日
 */
public class ContainsDuplicate
{
    public static void main(String[] args)
    {
        int[] nums= {1,2,5,3,3};
        System.out.println(containsDuplicate(nums));
    }
    
    // Make use of the feature of data structure: Set
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> set=new HashSet<Integer>();
        for(int i=0;i<nums.length;i++) {
            if(set.contains(nums[i]))
                return true;
            else
                set.add(nums[i]);
        }
        return false;
    }
}


```