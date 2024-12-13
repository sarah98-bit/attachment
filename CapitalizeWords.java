/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.capitalizewords;

/**
 *
 * @author swati love
 */
public class CapitalizeWords {
    public static void main(String[] args) {
        // Sample input string
        String input = "i love programming";
        
        // Call the method to capitalize the words
        String result = capitalizeWords(input);
        
        // Print the result
        System.out.println(result);
    }

    // Method to capitalize the first letter of each word in the string
    public static String capitalizeWords(String str) {
        // Split the string into words
        String[] words = str.split(" ");
        
        // StringBuilder to build the result
        StringBuilder result = new StringBuilder();
        
        // Loop through each word
        for (String word : words) {
            // Capitalize the first letter and append the rest of the word
            if (!word.isEmpty()) {
                result.append(Character.toUpperCase(word.charAt(0)))
                      .append(word.substring(1).toLowerCase())
                      .append(" ");
            }
        }
        
        // Return the result after trimming the trailing space
        return result.toString().trim();
    }
}

