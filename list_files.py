from dataclasses import dataclass
import os


@dataclass(slots=True)
class FileLister:
    directory: str
    search: str

    def list_files(self):
        return os.listdir(self.directory)

    def ends_with(self):
        for fn in os.listdir(self.directory):
            if fn.endswith(self.search):
                print(fn)


def main():
    f = FileLister(".", "py")
    print(f.list_files())
    print(f.ends_with())


if __name__ == "__main__":
    main()
