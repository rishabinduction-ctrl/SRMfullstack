package com.gdb.domain;

import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

/**
 * Loads account rules from properties files.
 * Each account type has its own properties file.
 */
public class AccountRulesPropertiesLoader {
    
    private static final String CONFIG_PATH = "/config/rules/";
    
    /**
     * Load rules for a specific account type from properties file.
     * @param accountType Account type (SAVINGS, CURRENT, etc.)
     * @return Map of tenure bucket → Rule
     */
    public static Map<Integer, AccountRulesEngine.Rule> loadRules(String accountType) {
        Map<Integer, AccountRulesEngine.Rule> rules = new HashMap<>();
        String propertyFile = CONFIG_PATH + accountType.toLowerCase() + ".properties";
        
        InputStream input = AccountRulesPropertiesLoader.class.getResourceAsStream(propertyFile);
        if (input == null) {
            input = AccountRulesPropertiesLoader.class.getResourceAsStream("config/rules/" + accountType.toLowerCase() + ".properties");
        }
        if (input == null) {
            input = Thread.currentThread().getContextClassLoader().getResourceAsStream("config/rules/" + accountType.toLowerCase() + ".properties");
        }

        try {
            if (input == null) {
                System.err.println("⚠️ Properties file not found: " + propertyFile);
                System.err.println("   Using default rules for " + accountType);
                return getDefaultRules(accountType);
            }
            
            Properties props = new Properties();
            props.load(input);
            input.close();
            
            // Get all bucket keys from properties (e.g., new, standard, premium, privilege)
            String[] bucketKeys = getBucketKeys(props);
            
            for (String bucketKey : bucketKeys) {
                // Read tenure value
                int tenure = Integer.parseInt(
                    props.getProperty("tenure.bucket." + bucketKey, "0"));
                
                // Read basic properties
                double minBalance = Double.parseDouble(
                    props.getProperty("min.balance." + bucketKey, "0"));
                double interestRate = Double.parseDouble(
                    props.getProperty("interest.rate." + bucketKey, "0"));
                String featureName = props.getProperty(
                    "feature.name." + bucketKey, "Unknown");
                
                // Create Rule object
                AccountRulesEngine.Rule rule = 
                    new AccountRulesEngine.Rule(minBalance, interestRate, featureName);
                
                // Load additional features dynamically by looking for keys ending with .<bucketKey>
                String suffix = "." + bucketKey;
                for (String key : props.stringPropertyNames()) {
                    if (key.endsWith(suffix)) {
                        String prefix = key.substring(0, key.length() - suffix.length());
                        
                        // Skip standard attributes already handled
                        if (prefix.equals("min.balance") || prefix.equals("interest.rate") ||
                            prefix.equals("feature.name") || prefix.equals("tenure.bucket")) {
                            continue;
                        }
                        
                        String value = props.getProperty(key);
                        String camelName = toCamelCase(prefix);
                        
                        Object parsedVal = parseValue(prefix, value);
                        rule.addFeature(camelName, parsedVal);
                        rule.addFeature(prefix, parsedVal);
                    }
                }
                
                rules.put(tenure, rule);
            }
            
            System.out.println("✅ Loaded rules for: " + accountType + 
                             " (" + rules.size() + " tenure buckets)");
            
        } catch (Exception e) {
            System.err.println("❌ Error loading rules for " + accountType + ": " + e.getMessage());
            return getDefaultRules(accountType);
        }
        
        return rules;
    }
    
    /**
     * Converts dot-separated property names to camelCase.
     * e.g., "overdraft.limit" -> "overdraftLimit"
     */
    private static String toCamelCase(String s) {
        StringBuilder sb = new StringBuilder();
        boolean capitalizeNext = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '.') {
                capitalizeNext = true;
            } else {
                if (capitalizeNext) {
                    sb.append(Character.toUpperCase(c));
                    capitalizeNext = false;
                } else {
                    sb.append(c);
                }
            }
        }
        return sb.toString();
    }

    private static Object parseValue(String prefix, String value) {
        if (value == null) return null;
        try {
            if (prefix.equals("overdraft.limit") || prefix.equals("penalty.percentage") || prefix.equals("daily.transfer.limit")) {
                return Double.parseDouble(value);
            }
            if (prefix.equals("lockin.months")) {
                return Integer.parseInt(value);
            }
            if (value.contains(".")) {
                return Double.parseDouble(value);
            }
            try {
                return Integer.parseInt(value);
            } catch (NumberFormatException e) {
                return value;
            }
        } catch (Exception e) {
            return value;
        }
    }
    
    /**
     * Extract all bucket keys from properties.
     * Keys like: tenure.bucket.new, tenure.bucket.standard, etc.
     */
    private static String[] getBucketKeys(Properties props) {
        return props.stringPropertyNames().stream()
            .filter(key -> key.startsWith("tenure.bucket."))
            .map(key -> key.substring("tenure.bucket.".length()))
            .toArray(String[]::new);
    }
    
    /**
     * Default rules if properties file not found.
     */
    private static Map<Integer, AccountRulesEngine.Rule> getDefaultRules(String accountType) {
        Map<Integer, AccountRulesEngine.Rule> defaultRules = new HashMap<>();
        AccountRulesEngine.Rule defaultRule = 
            new AccountRulesEngine.Rule(1000, 4.0, "Default " + accountType);
        defaultRules.put(0, defaultRule);
        return defaultRules;
    }
}
