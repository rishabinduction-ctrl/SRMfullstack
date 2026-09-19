package com.gdb.domain;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Account Rules Engine with Properties File Configuration.
 * Singleton pattern with hot-reload capability.
 * Dynamic rule sets loaded from external properties files.
 */
public class AccountRulesEngine {
    
    private static AccountRulesEngine instance;
    private Map<String, Map<Integer, Rule>> rulesMap;
    private boolean loaded = false;
    private String lastLoadTime;
    
    // Rule class - holds all data for a tenure bucket
    public static class Rule {
        private double minBalance;
        private double interestRate;
        private String featureName;
        private Map<String, Object> additionalFeatures;
        
        public Rule(double minBalance, double interestRate, String featureName) {
            this.minBalance = minBalance;
            this.interestRate = interestRate;
            this.featureName = featureName;
            this.additionalFeatures = new ConcurrentHashMap<>();
        }
        
        public double getMinBalance() { return minBalance; }
        public double getInterestRate() { return interestRate; }
        public String getFeatureName() { return featureName; }
        public Map<String, Object> getAdditionalFeatures() { return additionalFeatures; }
        
        public void addFeature(String key, Object value) {
            additionalFeatures.put(key, value);
        }
        
        @Override
        public String toString() {
            return String.format("Min: ₹%,.0f, Interest: %.2f%%, Feature: %s",
                               minBalance, interestRate, featureName);
        }
    }
    
    private AccountRulesEngine() {
        loadAllRules();
    }
    
    public static AccountRulesEngine getInstance() {
        if (instance == null) {
            synchronized (AccountRulesEngine.class) {
                if (instance == null) {
                    instance = new AccountRulesEngine();
                }
            }
        }
        return instance;
    }
    
    /**
     * Load all rules from properties files.
     */
    public synchronized void loadAllRules() {
        rulesMap = new ConcurrentHashMap<>();
        String[] accountTypes = {"SAVINGS", "CURRENT", "FIXEDDEPOSIT", "SALARY"};
        
        System.out.println("\n📂 Loading account rules from properties files...");
        System.out.println("-".repeat(50));
        
        for (String type : accountTypes) {
            Map<Integer, Rule> rules = AccountRulesPropertiesLoader.loadRules(type);
            if (rules != null && !rules.isEmpty()) {
                rulesMap.put(type, rules);
            }
        }
        
        loaded = true;
        lastLoadTime = java.time.LocalDateTime.now().toString();
        System.out.println("-".repeat(50));
        System.out.println("✅ All rules loaded successfully!");
        System.out.println("   Loaded at: " + lastLoadTime);
        System.out.println("   Account types: " + rulesMap.keySet());
    }
    
    /**
     * Hot reload - reload all rules without restarting the application.
     */
    public synchronized void reloadRules() {
        System.out.println("\n🔄 Reloading rules...");
        loadAllRules();
        System.out.println("✅ Rules reloaded successfully!");
    }
    
    // ===== Helper Methods =====
    
    private int getTenureBucket(int tenureYears) {
        if (tenureYears < 1) return 0;
        else if (tenureYears < 3) return 1;
        else if (tenureYears < 5) return 3;
        else return 5;
    }
    
    private Rule getRule(String accountType, int tenureYears) {
        String key = accountType.toUpperCase();
        Map<Integer, Rule> accountRules = rulesMap.get(key);
        if (accountRules == null) return null;
        
        int bucket = getTenureBucket(tenureYears);
        return accountRules.get(bucket);
    }
    
    public String getTenureBucketName(int tenureYears) {
        int bucket = getTenureBucket(tenureYears);
        switch (bucket) {
            case 0: return "NEW (0-1 year)";
            case 1: return "STANDARD (1-3 years)";
            case 3: return "PREMIUM (3-5 years)";
            case 5: return "PRIVILEGE (5+ years)";
            default: return "UNKNOWN";
        }
    }
    
    // ===== Public API Methods =====
    
    public double getMinimumBalance(String accountType, int tenureYears) {
        Rule rule = getRule(accountType, tenureYears);
        return rule != null ? rule.getMinBalance() : 0;
    }
    
    public double getInterestRate(String accountType, int tenureYears) {
        Rule rule = getRule(accountType, tenureYears);
        return rule != null ? rule.getInterestRate() : 0;
    }
    
    public String getFeatureName(String accountType, int tenureYears) {
        Rule rule = getRule(accountType, tenureYears);
        return rule != null ? rule.getFeatureName() : "Unknown Account";
    }
    
    public Object getAdditionalFeature(String accountType, int tenureYears, String key) {
        Rule rule = getRule(accountType, tenureYears);
        if (rule == null) return null;
        return rule.getAdditionalFeatures().get(key);
    }
    
    public double getDailyTransferLimit(String accountType, int tenureYears) {
        Object limit = getAdditionalFeature(accountType, tenureYears, "dailyTransferLimit");
        if (limit instanceof Double) {
            return (Double) limit;
        }
        return 0.0;
    }

    public boolean hasAccountType(String accountType) {
        return rulesMap.containsKey(accountType.toUpperCase());
    }
    
    public boolean isLoaded() {
        return loaded;
    }
    
    public String getLastLoadTime() {
        return lastLoadTime;
    }
    
    /**
     * Print all loaded rules.
     */
    public void printAllRules() {
        System.out.println("\n=== ALL ACCOUNT RULES (FROM PROPERTIES FILES) ===");
        for (String type : rulesMap.keySet()) {
            System.out.println("\n📁 " + type + ":");
            Map<Integer, Rule> rules = rulesMap.get(type);
            for (Map.Entry<Integer, Rule> entry : rules.entrySet()) {
                int bucket = entry.getKey();
                Rule rule = entry.getValue();
                String bucketName = getTenureBucketName(bucket);
                System.out.printf("  %-25s -> %s%n", bucketName, rule);
                
                // Print additional features if any
                if (!rule.getAdditionalFeatures().isEmpty()) {
                    System.out.print("    Features: ");
                    for (Map.Entry<String, Object> feat : rule.getAdditionalFeatures().entrySet()) {
                        System.out.print(feat.getKey() + "=" + feat.getValue() + " ");
                    }
                    System.out.println();
                }
            }
        }
    }
    
    /**
     * Get count of account types loaded.
     */
    public int getAccountTypeCount() {
        return rulesMap.size();
    }
}
