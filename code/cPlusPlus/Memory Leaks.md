Her er nogle **klassiske C++ kodeeksempler på memory leaks**, med korte forklaringer til hver.

---

### 1. Glemmer at frigive hukommelse (new uden delete)

```cpp
void leak() {
    int* ptr = new int(42);
    // delete ptr mangler
}
```

**Hvorfor lækker det?**
Hukommelsen allokeres på heapen, men frigives aldrig.

---

### 2. Tidlig return før delete

```cpp
int* createValue(bool fail) {
    int* value = new int(10);

    if (fail) {
        return nullptr; // delete value bliver aldrig kaldt
    }

    delete value;
    return nullptr;
}
```

---

### 3. Overskriver pointer uden at frigive gammel hukommelse

```cpp
void overwritePointer() {
    int* ptr = new int(5);
    ptr = new int(10); // første allocation er nu tabt
}
```

---

### 4. Manglende destructor cleanup i klasse

```cpp
class Leaky {
public:
    Leaky() {
        data = new int[100];
    }

    // Destructor mangler
private:
    int* data;
};
```

**Problem**
Når objektet destrueres, bliver `data` aldrig frigivet.

---

### 5. Forkert delete type (new[] men delete)

```cpp
void wrongDelete() {
    int* arr = new int[50];
    delete arr; // skulle være delete[]
}
```

Dette kan føre til undefined behavior og ofte leaks.

---

### 6. Exception før delete

```cpp
void exceptionLeak() {
    int* data = new int(123);
    throw std::runtime_error("Boom");
    delete data; // nås aldrig
}
```

---

### 7. C-style malloc uden free

```cpp
void cStyleLeak() {
    int* ptr = (int*)malloc(sizeof(int) * 10);
    // free(ptr) mangler
}
```

---

### 8. Cirkulære referencer med shared_ptr

```cpp
#include <memory>

struct B;

struct A {
    std::shared_ptr<B> b;
};

struct B {
    std::shared_ptr<A> a;
};

void circularLeak() {
    auto a = std::make_shared<A>();
    auto b = std::make_shared<B>();
    a->b = b;
    b->a = a;
}
```

**Hvorfor lækker det?**
Reference count bliver aldrig 0.

---

## Best practice for at undgå leaks

```cpp
#include <memory>

void noLeak() {
    auto ptr = std::make_unique<int>(42);
}
```

* Brug **RAII**
* Foretræk `std::unique_ptr` og `std::shared_ptr`
* Undgå rå `new` og `delete`
* Brug værktøjer som **Valgrind**, **ASan**, eller **Visual Studio Diagnostic Tools**

