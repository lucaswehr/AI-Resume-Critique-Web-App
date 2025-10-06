CXX = g++
CXXFLAGS = -std=c++11
SOURCE = $(wildcard *.cpp)

TARGET = program
$(TARGET): $(SOURCE)
		$(CXX) $(CXXFLAGS)  $(SOURCE) -o $(TARGET)

clean:
		rm -f $(TARGET)
