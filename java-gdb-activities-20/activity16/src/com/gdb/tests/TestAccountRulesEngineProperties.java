package com.gdb.tests;

import com.gdb.domain.AccountRulesEngine;

public class TestAccountRulesEngineProperties {
    
    private static void printSeparator() {
        System.out.println("-".repeat(60));
    }
    
    private static void printHeader(String title) {
        System.out.println("\n>>> " + title);
        printSeparator();
    }
    
    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("  ACCOUNT RULES ENGINE - ACTIVITY 14 (PROPERTIES)");
        System.out.println("  Rules Loaded from External Properties Files");
        System.out.println("=".repeat(60));
        
        AccountRulesEngine engine = AccountRulesEngine.getInstance();
        
        // Show loaded status
        System.out.println("\n📋 Engine Status:");
        System.out.println("  Loaded: " + engine.isLoaded());
        System.out.println("  Load Time: " + engine.getLastLoadTime());
        System.out.println("  Account Types: " + engine.getAccountTypeCount());
        
        // Print all rules
        engine.printAllRules();
        
        // Test 1: Savings Account
        printHeader("Test 1: Savings Account Rules (From Properties)");
        System.out.printf("%-12s %-20s %-15s %-15s %-20s%n", 
                         "Tenure", "Bucket", "Min Balance", "Interest", "Feature");
        printSeparator();
        
        int[] tenures = {0, 1, 2, 3, 4, 5, 6};
        for (int tenure : tenures) {
            String bucket = engine.getTenureBucketName(tenure);
            double minBal = engine.getMinimumBalance("SAVINGS", tenure);
            double interest = engine.getInterestRate("SAVINGS", tenure);
            String feature = engine.getFeatureName("SAVINGS", tenure);
            System.out.printf("%d years     %-18s ₹%,9.0f    %.2f%%        %-20s%n",
                             tenure, bucket, minBal, interest, feature);
        }
        
        // Test 2: Current Account
        printHeader("Test 2: Current Account Rules (From Properties)");
        System.out.printf("%-12s %-20s %-15s %-15s %-15s%n", 
                         "Tenure", "Bucket", "Min Balance", "Interest", "Overdraft");
        printSeparator();
        
        int[] currentTenures = {0, 1, 2, 3, 4};
        for (int tenure : currentTenures) {
            String bucket = engine.getTenureBucketName(tenure);
            double minBal = engine.getMinimumBalance("CURRENT", tenure);
            double interest = engine.getInterestRate("CURRENT", tenure);
            double overdraft = (double) engine.getAdditionalFeature("CURRENT", tenure, "overdraftLimit");
            System.out.printf("%d years     %-18s ₹%,9.0f    %.2f%%        ₹%,9.0f%n",
                             tenure, bucket, minBal, interest, overdraft);
        }
        
        // Test 3: Fixed Deposit
        printHeader("Test 3: Fixed Deposit Rules (From Properties)");
        System.out.printf("%-12s %-20s %-15s %-15s %-15s %-15s%n", 
                         "Tenure", "Bucket", "Min Balance", "Interest", "Lock-in", "Penalty");
        printSeparator();
        
        for (int tenure : tenures) {
            String bucket = engine.getTenureBucketName(tenure);
            double minBal = engine.getMinimumBalance("FIXEDDEPOSIT", tenure);
            double interest = engine.getInterestRate("FIXEDDEPOSIT", tenure);
            int lockin = (int) engine.getAdditionalFeature("FIXEDDEPOSIT", tenure, "lockinMonths");
            double penalty = (double) engine.getAdditionalFeature("FIXEDDEPOSIT", tenure, "penaltyPercentage");
            System.out.printf("%d years     %-18s ₹%,9.0f    %.2f%%        %d months    %.2f%%%n",
                             tenure, bucket, minBal, interest, lockin, penalty);
        }
        
        // Test 4: Salary Account
        printHeader("Test 4: Salary Account Rules (From Properties)");
        System.out.printf("%-12s %-20s %-15s %-15s %-15s %-30s%n", 
                         "Tenure", "Bucket", "Min Balance", "Interest", "Status", "Benefits");
        printSeparator();
        
        for (int tenure : tenures) {
            String bucket = engine.getTenureBucketName(tenure);
            double minBal = engine.getMinimumBalance("SALARY", tenure);
            double interest = engine.getInterestRate("SALARY", tenure);
            String status = (String) engine.getAdditionalFeature("SALARY", tenure, "privilegeStatus");
            String benefits = (String) engine.getAdditionalFeature("SALARY", tenure, "benefits");
            System.out.printf("%d years     %-18s ₹%,9.0f    %.2f%%        %-15s %-30s%n",
                             tenure, bucket, minBal, interest, status, benefits);
        }
        
        // Test 5: Hot Reload Demonstration
        printHeader("Test 5: Hot Reload Feature");
        System.out.println("The rules engine supports hot reloading!");
        System.out.println("To test hot reload:");
        System.out.println("  1. Modify any .properties file");
        System.out.println("  2. Call engine.reloadRules()");
        System.out.println("  3. Changes take effect immediately without restart");
        System.out.println();
        System.out.println("💡 This is a production-grade feature for:");
        System.out.println("   - Updating interest rates without deployment");
        System.out.println("   - A/B testing different rule sets");
        System.out.println("   - Fixing configuration errors quickly");
        
        // Test 6: Properties File Benefits
        printHeader("Test 6: Properties File vs Hardcoded");
        System.out.println("✅ Configuration Externalization Benefits:");
        System.out.println("   1. No code changes for rule updates");
        System.out.println("   2. Business teams can update rules");
        System.out.println("   3. Different environments (Dev/Prod) can have different rules");
        System.out.println("   4. Version control for configuration");
        System.out.println("   5. Easy to audit rule changes");
        System.out.println("   6. Hot reload without application restart");
        
        System.out.println();
        System.out.println("=".repeat(60));
        System.out.println("  ACTIVITY 14 TEST COMPLETED!");
        System.out.println("  🎯 Configuration-Driven Architecture Achieved!");
        System.out.println("=".repeat(60));
    }
}
