# 📋 Registry Schema Documentation

This document describes the JSON Schema structure and validation rules for the MCP Servers Hub registry.

> **🎯 Specialization Note**: This registry is specifically designed for **Python MCP server projects** created using MCP Factory

## 🎯 Schema Overview

[`registry-schema.json`](registry-schema.json) defines the strict data structure for [`registry.json`](registry.json), ensuring:

- ✅ **Python Project Specific** - Specialized for Python MCP servers
- ✅ **Data Type Correctness** - All field types meet expectations
- ✅ **Format Standardization** - URLs, dates and other formats are standardized  
- ✅ **Required Field Completeness** - Prevents missing critical information
- ✅ **String Length Limits** - Avoids overly long descriptions and names
- ✅ **Enumeration Constraints** - Limits tag and license options

## 📊 Data Structure

### Top-level Structure

```json
{
  "$schema": "./registry-schema.json",
  "version": "1.0.0",                    // Required: semantic version number
  "updated": "2025-07-01T00:00:00Z",     // Required: ISO 8601 timestamp
  "projects": [ /* project array */ ]    // Required: project list
}
```

### Project Structure

```json
{
  "name": "database-tools",                    // Required: project name (lowercase, kebab-case)
  "author": "github-username",                // Required: GitHub username
  "description": "Database operations MCP server", // Required: 10-200 characters
  "repository": "https://github.com/user/repo",   // Required: GitHub repository URL
  "language": "python",                       // Required: fixed as "python"
  "python_version": "3.10",                  // Required: minimum Python version
  "tags": ["database", "tools"],             // Required: predefined tag list
  "license": "MIT",                          // Required: license (enum value)
  "created": "2025-07-01T00:00:00Z",        // Required: creation timestamp
  "mcp_factory": {                           // Optional: MCP Factory metadata
    "version": "1.0.0",
    "template": "database"
  },
  "homepage": "https://...",                  // Optional: project homepage
  "documentation": "https://..."             // Optional: documentation link
}
```

## 🔍 Validation Rules

### Project Name (`name`)
- **Format**: lowercase letters, numbers, hyphens
- **Pattern**: `^[a-z0-9][a-z0-9-]*[a-z0-9]$`
- **Length**: 3-50 characters
- **Examples**: `database-tools`, `file-manager`, `ai-assistant`
- **Note**: ❌ No longer requires `mcp-` prefix

### GitHub Username (`author`)
- **Format**: GitHub username rules
- **Pattern**: `^[a-zA-Z0-9]([a-zA-Z0-9-]){0,38}$`
- **Examples**: `acnet`, `user-name`, `Company123`

### Repository URL (`repository`)
- **Format**: Must be GitHub repository URL
- **Pattern**: `^https://github\.com/[username]/[repository]$`
- **Example**: `https://github.com/ACNet-AI/mcp-factory`

### Programming Language (`language`)
- **Value**: Fixed as `"python"`
- **Description**: This registry specifically supports Python projects

### Python Version (`python_version`)
- **Format**: major.minor version
- **Supported Versions**: `3.10`, `3.11`, `3.12`, `3.13`
- **Pattern**: `^3\.(10|11|12|13)$`
- **Examples**: `"3.10"`, `"3.12"`

### Tags (`tags`)
- **Count**: 1-8 tags
- **Type**: Predefined enumeration values
- **Available Tags**:
  ```
  database, api, tools, automation, data, web, files,
  ai, ml, cloud, monitoring, security, testing, dev-tools,
  productivity, integration, analytics, communication, finance,
  media, storage, search, notifications, workflow
  ```

### License (`license`)
**Supported Licenses**:
- `MIT` - MIT License (most popular permissive license)
- `Apache-2.0` - Apache 2.0 License (enterprise-friendly with patent protection)
- `GPL-3.0` - GPL v3 License (copyleft open source license)
- `BSD-3-Clause` - BSD 3-Clause License (commonly used in academia)
- `ISC` - ISC License (modern project preference, similar to MIT but more concise)
- `other` - Other licenses (for licenses not in the above list)

### MCP Factory Metadata (`mcp_factory`)
**Optional fields**, including:
- `version`: MCP Factory version number
- `template`: Template type used
  - Optional values: `basic`, `advanced`, `database`, `api`, `tool`

### Timestamps
- **Format**: ISO 8601
- **Example**: `2025-07-01T00:00:00Z`

## 🧪 Local Validation

```bash
# Recommended: Use validation script (includes detailed information)
python validate.py

# Or: Use uv to run
uv run python validate.py

# Or: Use jsonschema directly (schema validation only)
python -c "
import json, jsonschema
with open('registry-schema.json') as s, open('registry.json') as r:
    jsonschema.validate(json.load(r), json.load(s))
print('✅ Schema validation passed')
"
```

## 🔄 CI/CD Integration

GitHub Actions automatically runs the following validations:

1. **JSON Format Validation** - Ensures JSON syntax is correct
2. **Schema Validation** - Validates data structure and types
3. **Python Project Validation** - Ensures it's a Python project
4. **Repository Accessibility Check** - Verifies GitHub repository exists
5. **Duplicate Check** - Prevents duplicate project names and repositories

## 📋 Complete Example

```json
{
  "$schema": "./registry-schema.json",
  "version": "1.0.0",
  "updated": "2025-07-03T00:00:00Z",
  "projects": [
    {
      "name": "database-tools",
      "author": "acnet",
      "description": "Powerful database operations and query tools for MCP servers",
      "repository": "https://github.com/acnet/database-tools",
      "language": "python",
      "python_version": "3.10",
      "tags": ["database", "tools", "api"],
      "license": "MIT",
      "created": "2025-07-03T00:00:00Z",
      "mcp_factory": {
        "version": "1.0.0",
        "template": "database"
      },
      "homepage": "https://acnet.github.io/database-tools",
      "documentation": "https://github.com/acnet/database-tools#readme"
    }
  ]
}
```

## 📝 Schema Updates

To modify the Schema:

1. Update [`registry-schema.json`](registry-schema.json)
2. Update this documentation
3. Ensure backward compatibility
4. Run complete validation tests

---

## 💡 Best Practices

- **Project Name**: Use descriptive, easy-to-understand names (no need for `mcp-` prefix)
- **Description**: Concisely and clearly describe MCP server functionality and purpose
- **Tags**: Choose the most relevant tags from the predefined list
- **Python Version**: Select the minimum version actually required by your project
- **Documentation**: Provide clear README and usage instructions

For more information, please refer to [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md). 