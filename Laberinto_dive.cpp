#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <chrono>
#include <string>

using namespace std;

//Creamos la celda unitaria
struct Cell{
    bool visited = false;
    bool top = true, bottom = true, left = true, right = true;
    bool path = false;
};

// Direcciones que puede hacer[Arriba, Abajo, Izquierda, Derecha]
vector<pair<int,int>> directrions = {{-1,0}, {1,0}, {0,-1}, {0,1}};

//Generamos las celdas antes de hacer el laberinto
void initMaze(vector<vector<Cell>>& maze, int N) {
    maze = vector<vector<Cell>>(N, vector<Cell>(N));
}

//generamos los booleanos para la matriz
void initVisited(vector<vector<bool>>& visited, int N){
    visited = vector<vector<bool>>(N, vector<bool>(N, false));
}

//Empezamos a hacer los caminos del laberinto 

void generateMaze(vector<vector<Cell>>& maze, int x, int y, int N) {
    maze[x][y].visited = true;
    auto dir = directrions;
    shuffle(dir.begin(), dir.end(), default_random_engine(random_device{}()));

    for(auto [dx,dy] : dir) {
        int nx = x + dx, ny = y + dy;
        if (nx >= 0 && ny >= 0 && nx < N && ny < N && !maze[nx][ny].visited) {
            if (dx == -1) {
                maze[x][y].top = false;
                maze[nx][ny]. bottom = false;
            } else if (dx == 1) {
                maze[x][y].bottom = false;
                maze[nx][ny].top = false;
            } else if (dy == -1) {
                maze[x][y].left = false;
                maze[nx][ny].right = false;
            } else if (dy == 1) {
                maze[x][y].right = false;
                maze[nx][ny].left = false;
            }
            generateMaze(maze, nx, ny, N);
            
        }
    }
}

// Hacemos el algoritmo de resolucion del laberinto
bool solveBacktraking(vector<vector<Cell>>& maze,vector<vector<bool>>& visited, int x, int y, int N) {
    if (x == N-1 && y == N-1) {
        maze[x][y].path = true;
        return true;
    }
    visited[x][y] = true;

    for (auto [dx, dy] : directrions) {
        int nx = x + dx, ny = y + dy;
        if (nx >= 0 && ny >= 0 && nx < N && ny < N && !visited[nx][ny]) {
            if ((dx == -1 && !maze[x][y].top) ||
                (dx == 1 && !maze[x][y].bottom) ||
                (dy == -1 && !maze[x][y].left) ||
                (dy == 1 && !maze[x][y].right)) {
                    if (solveBacktraking(maze, visited, nx, ny, N)) {
                        maze[x][y].path = true;
                        return true;
                    }
                }
        }
    }
    return false;
}


/*void clearPath(vector<vector<Cell>>& maze, vector<vector<bool>>& visited, int N) {
    initVisited (visited, N);
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            maze[i][j].path = false;
    
}*/

void printMaze(vector<vector<Cell>>& maze, int N) {
    cout << "+";
    for (int i = 0; i < N; i++) cout << "---+";
    cout << "\n";

    for (int i = 0; i < N; i++) {
        cout << "|";
        for (int j = 0; j < N; j++) {
            if (i == 0 && j == 0)
                cout << " E ";
            else if (i == N - 1 && j == N - 1)
                cout << " S ";
            else if (maze[i][j].path)
                cout << " * ";
            else
                cout << "   ";
            cout << (maze[i][j].right ? "|" : " ");
        }
        cout << "\n+";
        for (int j = 0; j < N; j++) {
            cout << (maze[i][j].bottom ? "---" : "   ") << "+";
        }
        cout << "\n";
    }
}

int main() {
    int N = 10;
    
    vector<vector<Cell>> maze;
    vector<vector<bool>> visited;

    auto start = chrono::high_resolution_clock::now();

    // Inicializa el laberinto y la matriz de visitados
    initMaze(maze, N);
    initVisited(visited, N);
    
    // Generara el laberinto
    generateMaze(maze, 0, 0, N);

    // Limpiar el path antes de resolver
    // clearPath(maze, visited, N);

    // Resouelve el laberinto con backtraking
    solveBacktraking(maze, visited, 0, 0, N);

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> diff = end - start;

    // Mostrar resultados
    printMaze(maze, N);
    cout << "\nAlgoritmo usado: Backtracking\n";
    cout << "Tiempo de ejecucion: " << diff.count() << " segundos\n";
    
    return 0;
}

