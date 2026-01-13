public class AuthDemo {

    // Hardcoded user information
    static String currentUsername = "Nicholas Pickett";
    static String currentRole = "admin"; 
    // print statement to show current user and role
    public static void main(String[] args) {
        System.out.println("Logged in as: " + currentUsername);
        System.out.println("Role: " + currentRole);
        System.out.println();

        accessUserFeature();
        accessAdminFeature();
    }

    // Changes roles into permissions
    static int getRoleLevel(String role) {
        return switch (role) {
            case "admin" -> 2;
            case "user" -> 1;
            default -> 0;
        };
    }

    // Checks for user-level access
    static void accessUserFeature() {
        if (getRoleLevel(currentRole) >= 1) {
            System.out.println("User access granted: Viewing personal dashboard.");
        } else {
            System.out.println("User access denied.");
        }
    }

    // Admin-only access
    static void accessAdminFeature() {
        if (getRoleLevel(currentRole) >= 2) {
            System.out.println("Admin access granted: Viewing system settings.");
        } else {
            System.out.println("Admin access denied.");
        }
    }
}

// This program demonstrates a simple role-based access control system using Java.
// This programs also demonstrates confidentiality of the CIA triad by restricting access to certain features based on user roles.
// Meaning only users with sufficient privileges can access sensitive information or functionalities.
