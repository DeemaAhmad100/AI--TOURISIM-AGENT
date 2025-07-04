"""
🧹 Project Cleanup Tool
Organize and clean up unnecessary files in the AI Travel Platform project
"""

import os
import shutil
from pathlib import Path

class ProjectCleaner:
    """Clean up unnecessary files and organize the project"""
    
    def __init__(self, project_path):
        self.project_path = Path(project_path)
        
        # Define file categories
        self.essential_files = {
            # Core platform files
            "enhanced_travel_platform.py",
            "travel_agent.py", 
            "database_schema.py",
            "database_schema_updater.py",
            
            # Configuration
            ".env",
            "requirements.txt",
            "config.py",
            
            # Documentation
            "README.md",
            "LICENSE",
            "SCHEMA_OVERVIEW.md",
            
            # Enhanced features
            "enhanced_features/",
            
            # Recent useful scripts
            "final_enhanced_demo.py",
            "schema_inspector.py",
            "database_population_script.py",
            "compatible_database_population.py"
        }
        
        self.demo_test_files = {
            # Demo files
            "enhanced_intelligence_demo.py",
            "enhanced_system_demo.py", 
            "complete_demo.py",
            "quick_demo.py",
            "interactive_demo.py",
            "experience_demo.py",
            "malaysia_demo.py",
            "success_demonstration.py",
            "final_platform_demo.py",
            
            # Test files
            "test_config.py",
            "test_database.py", 
            "test_enhanced_agents.py",
            "test_enhanced_intelligence.py",
            "test_enhanced_system.py",
            "simple_test.py",
            "final_test.py",
            "comprehensive_test.py",
            "final_integration_test.py",
            
            # Check/utility scripts
            "check_current_ids.py",
            "check_destinations.py", 
            "check_tables.py",
            "check_travel_history.py",
            "database_inspector.py",
            "minimal_data_addition.py",
            "simple_database_population.py",
            "view_demo_data.py"
        }
        
        self.temp_output_files = {
            # Generated output files
            "enhanced_intelligence_demo_20250701_143930.txt",
            "enhanced_intelligence_demo_20250701_144043.txt", 
            "enhanced_intelligence_demo_20250701_144241.txt",
            "travel_plan_qatar_20250630_033326.txt",
            "travel_plan_turkey_20250628_162805.txt"
        }
        
        self.github_documentation = {
            # GitHub/Documentation files
            "CHANGELOG.md",
            "CONTRIBUTING.md", 
            "README_COMPLETE.md",
            "README_GITHUB_OPTIMIZED.md",
            "RELEASE_NOTES.md",
            "SECURITY.md",
            "PROJECT_COMPLETION_SUMMARY.md",
            "COMPLETE_GITHUB_SETUP.txt",
            "FINAL_UPLOAD_COMMANDS.txt",
            "github_setup_commands.txt",
            "GITHUB_SETUP_COMPLETE.md",
            "GITHUB_STRATEGY.md", 
            "GITHUB_UPLOAD_COMMANDS.txt",
            "INTEGRATION_COMPLETE.md"
        }
        
        self.alternate_configs = {
            # Alternative config files
            ".env.example",
            ".env_new",
            ".gitignore_optimized",
            "requirements_enhanced.txt",
            "pyproject.toml"
        }
        
        self.utility_scripts = {
            # Utility/helper scripts
            "add_missing_attractions.py",
            "demo_config_integration.py",
            "env_setup_helper.py",
            "intent_detection.py",
            "main_app.py",
            "streamlit_ui.py",
            "world_travel_expert.py"
        }
    
    def analyze_project(self):
        """Analyze the current project structure"""
        print("🔍 Analyzing project structure...")
        print("="*60)
        
        all_files = [f for f in os.listdir(self.project_path) if os.path.isfile(os.path.join(self.project_path, f))]
        all_dirs = [d for d in os.listdir(self.project_path) if os.path.isdir(os.path.join(self.project_path, d))]
        
        print(f"📁 Total files: {len(all_files)}")
        print(f"📂 Total directories: {len(all_dirs)}")
        print()
        
        categorized = {
            "essential": [],
            "demo_test": [],
            "temp_output": [],
            "github_docs": [],
            "alt_configs": [],
            "utilities": [],
            "uncategorized": []
        }
        
        for file in all_files:
            if file in self.essential_files:
                categorized["essential"].append(file)
            elif file in self.demo_test_files:
                categorized["demo_test"].append(file)
            elif file in self.temp_output_files:
                categorized["temp_output"].append(file)
            elif file in self.github_documentation:
                categorized["github_docs"].append(file)
            elif file in self.alternate_configs:
                categorized["alt_configs"].append(file)
            elif file in self.utility_scripts:
                categorized["utilities"].append(file)
            else:
                categorized["uncategorized"].append(file)
        
        # Show categorization
        print("📋 FILE CATEGORIZATION:")
        print("-" * 60)
        
        print(f"\n✅ ESSENTIAL FILES ({len(categorized['essential'])}):")
        for file in sorted(categorized['essential']):
            print(f"   • {file}")
        
        print(f"\n🧪 DEMO/TEST FILES ({len(categorized['demo_test'])}):")
        for file in sorted(categorized['demo_test']):
            print(f"   • {file}")
        
        print(f"\n📄 TEMP OUTPUT FILES ({len(categorized['temp_output'])}):")
        for file in sorted(categorized['temp_output']):
            print(f"   • {file}")
        
        print(f"\n📚 GITHUB/DOCS ({len(categorized['github_docs'])}):")
        for file in sorted(categorized['github_docs']):
            print(f"   • {file}")
        
        print(f"\n⚙️ ALT CONFIGS ({len(categorized['alt_configs'])}):")
        for file in sorted(categorized['alt_configs']):
            print(f"   • {file}")
        
        print(f"\n🔧 UTILITIES ({len(categorized['utilities'])}):")
        for file in sorted(categorized['utilities']):
            print(f"   • {file}")
        
        if categorized['uncategorized']:
            print(f"\n❓ UNCATEGORIZED ({len(categorized['uncategorized'])}):")
            for file in sorted(categorized['uncategorized']):
                print(f"   • {file}")
        
        print(f"\n📂 DIRECTORIES:")
        for dir_name in sorted(all_dirs):
            print(f"   • {dir_name}/")
        
        return categorized
    
    def recommend_cleanup(self, categorized):
        """Recommend files for deletion"""
        print("\n" + "="*60)
        print("🗑️ CLEANUP RECOMMENDATIONS")
        print("="*60)
        
        # Safe to delete
        safe_to_delete = (
            categorized['temp_output'] + 
            categorized['demo_test'] +
            list(categorized['github_docs'])[:5]  # Keep some docs
        )
        
        # Consider deleting
        consider_deleting = (
            categorized['alt_configs'] +
            categorized['utilities']
        )
        
        print("✅ SAFE TO DELETE (temp/demo files):")
        for file in safe_to_delete:
            file_path = self.project_path / file
            if file_path.exists():
                size = file_path.stat().st_size
                print(f"   🗑️ {file} ({size} bytes)")
        
        print(f"\n🤔 CONSIDER DELETING (alternative/utility files):")
        for file in consider_deleting:
            file_path = self.project_path / file
            if file_path.exists():
                size = file_path.stat().st_size
                print(f"   ⚠️ {file} ({size} bytes)")
        
        print(f"\n🔒 KEEP (essential files):")
        for file in categorized['essential']:
            file_path = self.project_path / file
            if file_path.exists():
                print(f"   ✅ {file}")
        
        return safe_to_delete, consider_deleting
    
    def delete_files(self, files_to_delete, confirm=True):
        """Delete specified files"""
        if not files_to_delete:
            print("No files to delete.")
            return
        
        print(f"\n🗑️ PREPARING TO DELETE {len(files_to_delete)} FILES:")
        for file in files_to_delete:
            print(f"   • {file}")
        
        if confirm:
            response = input(f"\n❓ Delete these {len(files_to_delete)} files? (y/n): ").lower()
            if response != 'y':
                print("❌ Deletion cancelled.")
                return
        
        deleted_count = 0
        for file in files_to_delete:
            file_path = self.project_path / file
            try:
                if file_path.exists():
                    file_path.unlink()
                    print(f"✅ Deleted: {file}")
                    deleted_count += 1
                else:
                    print(f"⚠️ Not found: {file}")
            except Exception as e:
                print(f"❌ Error deleting {file}: {e}")
        
        print(f"\n🎉 Successfully deleted {deleted_count} files!")
    
    def create_backup(self, files_to_backup):
        """Create backup of important files before deletion"""
        backup_dir = self.project_path / "backup_before_cleanup"
        backup_dir.mkdir(exist_ok=True)
        
        print(f"💾 Creating backup in: {backup_dir}")
        
        for file in files_to_backup:
            file_path = self.project_path / file
            if file_path.exists():
                try:
                    shutil.copy2(file_path, backup_dir / file)
                    print(f"✅ Backed up: {file}")
                except Exception as e:
                    print(f"❌ Backup error for {file}: {e}")

def main():
    """Main cleanup interface"""
    project_path = Path.cwd()
    cleaner = ProjectCleaner(project_path)
    
    print("🧹 AI Travel Platform - Project Cleanup Tool")
    print("="*60)
    print(f"📁 Project directory: {project_path}")
    print()
    
    # Analyze project
    categorized = cleaner.analyze_project()
    
    # Get recommendations
    safe_to_delete, consider_deleting = cleaner.recommend_cleanup(categorized)
    
    print("\n🎯 CLEANUP OPTIONS:")
    print("1. Delete temp/demo files (safe)")
    print("2. Delete temp/demo + alternative configs")
    print("3. Custom selection")
    print("4. Just show analysis (no deletion)")
    print("5. Exit")
    
    choice = input("\n🔹 Choose option (1-5): ").strip()
    
    if choice == "1":
        cleaner.delete_files(safe_to_delete)
    elif choice == "2":
        cleaner.delete_files(safe_to_delete + consider_deleting)
    elif choice == "3":
        print("Custom selection not implemented yet.")
    elif choice == "4":
        print("✅ Analysis complete. No files deleted.")
    else:
        print("👋 Cleanup cancelled.")

if __name__ == "__main__":
    main()
