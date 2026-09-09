# File Copy Utility (`second.c`)

A simple command-line utility written in C that copies the contents of one file to another.

## Description
This program reads a source file character-by-character and writes the output to a specified destination file. It provides basic error handling for missing arguments and file access issues.

## Compilation
You can compile `second.c` using a standard C compiler like `gcc`:

```bash
gcc second.c -o copy_file
```

## Usage
Run the compiled executable with two arguments: the source file and the destination file.

```bash
./copy_file <source_file> <destination_file>
```

### Example
```bash
./copy_file input.txt output.txt
```

## Error Handling
- **Missing arguments:** The program requires exactly two arguments. If fewer are provided, it prompts: `Plz input 2 arguments, src and destination files`.
- **Invalid source file:** If the source file cannot be opened (e.g., does not exist), it displays: `Input file is emptry! error!`.
- **Invalid de
