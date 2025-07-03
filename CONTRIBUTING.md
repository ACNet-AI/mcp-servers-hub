# 🤝 Contributing Guide

Welcome to contribute to the MCP Servers Hub ecosystem! This guide covers detailed steps for project publishing, technical limitation analysis, and solutions.

> **📋 Current Status**: Only supports Python MCP server projects created using mcp-factory

## 🚀 Publishing MCP Server Projects

### 🎯 mcp-factory Project Publishing (Currently the Only Supported Method)

#### 📦 **Standard Publishing Process**

```bash
# 1. Install tools
pip install mcp-factory

# 2. Create project
mcp-factory init my-server
cd my-server

# 3. Develop functionality
# Implement features in tools/, resources/, prompts/ directories

# 4. One-click publish
mcp-factory project publish
```

#### 🏗️ **Project Structure Requirements**

```
my-mcp-server/
├── config.yaml             # MCP server configuration
├── pyproject.toml          # Python project configuration (required)
├── README.md               # Project documentation
├── tools/                  # Tool implementation directory
├── resources/              # Resource implementation directory
└── prompts/                # Prompt template directory
```

## ⚠️ Technical Limitation Analysis

### 🚫 **Currently Unsupported Project Types**

The mcp-factory publisher actively rejects non-Python projects:

```python
# Source: mcp_factory/project/publisher.py
if (project_path / "package.json").exists():
    raise PublishError("Cannot publish JavaScript project - mcp-factory only supports Python MCP servers")
```

**Unsupported Projects:**
- ❌ Node.js/JavaScript (package.json)
- ❌ Go (go.mod) 
- ❌ Rust (Cargo.toml)
- ❌ Other language MCP servers

### 🛣️ **Multi-language Support Roadmap**

**Phase 1: Node.js/TypeScript**
- [ ] Modify publisher to remove JavaScript restrictions
- [ ] Extend project validation to support `package.json`
- [ ] Add Node.js project templates

**Phase 2: Universal Language Support**
- [ ] Standard MCP protocol project detection
- [ ] Multi-language metadata extraction
- [ ] Reduce dependency on mcp-factory

## 🔧 Solutions for Other Language Projects

### 📋 **Currently Viable Options**

**🔄 Option A: Port to Python (Recommended)**
```bash
# Create Python version using mcp-factory
mcp-factory init my-server-python
# Port existing functionality to Python implementation
# One-click publish to ecosystem
mcp-factory project publish
```

**⏳ Option B: Wait for Multi-language Support**
- Follow mcp-factory project updates
- Maintain project independently for now
- Wait for official multi-language support

**🤝 Option C: Contribute Multi-language Support**
- Modify `mcp_factory/project/publisher.py` to remove language restrictions
- Extend project validator to support multiple languages
- Submit PR to help the community gain broader support

### 🔄 **Project Migration Guide**

**Migrating from other languages to Python:**

1. **Create mcp-factory project template**
   ```bash
   mcp-factory init my-server-python
   ```

2. **Re-implement core functionality**
   - Implement tool functions in `tools/` directory
   - Provide resource access in `resources/` directory
   - Define prompt templates in `prompts/` directory

3. **Configure and publish**
   ```bash
   # Test project structure
   mcp-factory project validate
   
   # Publish to ecosystem
   mcp-factory project publish
   ```

## 🏗️ Contributing Platform Code

### Extending Multi-language Support

If you want to help implement Node.js/Go/Rust language support:

```bash
# Fork and clone mcp-factory repository
git clone https://github.com/ACNet-AI/mcp-factory.git

# Main files to modify:
# - mcp_factory/project/publisher.py (remove language restrictions)
# - mcp_factory/project/constants.py (add new language configurations)
# - mcp_factory/project/template.py (add new language templates)
```

## 📋 Project Requirements

### ✅ **Basic Requirements (Auto-validated)**
- mcp-factory project structure (config.yaml + tools/resources/prompts/)
- Valid pyproject.toml configuration
- Detailed README.md documentation
- Correct MCP dependency configuration

### 🌟 **Recommended Practices**
- Include unit tests and usage examples
- Choose appropriate project categories and tags
- Provide detailed API documentation

## 📞 Getting Help

- **mcp-factory Issues**: [GitHub Issues](https://github.com/ACNet-AI/mcp-factory/issues)
- **Registry Issues**: [mcp-servers-hub Issues](https://github.com/ACNet-AI/mcp-servers-hub/issues)  
- **Community Discussion**: [GitHub Discussions](https://github.com/ACNet-AI/mcp-servers-hub/discussions)

---

<div align="center">

**Thank you for contributing to the MCP server ecosystem!** 🎉

**Recommended Starting Point**: [Create your first project using mcp-factory](https://github.com/ACNet-AI/mcp-factory)

[Browse Registry](registry.json) • [Ecosystem Architecture](README.md) • [Community Discussion](https://github.com/ACNet-AI/mcp-servers-hub/discussions)

</div> 