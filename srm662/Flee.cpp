#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
#define SZY

class Vector3{
  public:
	Vector3():x(0), y(0), z(0){
		
	}
    Vector3(float fx, float fy, float fz)
        :x(fx), y(fy), z(fz){
    }

    // Subtract
    Vector3 operator - (const Vector3& v) const{
        return Vector3(x - v.x, y - v.y, z - v.z) ;
    }

    // Dot product
    float Dot(const Vector3& v) const{
        return x * v.x + y * v.y + z * v.z ;
    }

    // Cross product
    Vector3 Cross(const Vector3& v) const{
        return Vector3(
            y * v.z - z * v.y,
            z * v.x - x * v.z,
            x * v.y - y * v.x ) ;
    }
	
  public:
    float x, y, z ;
};
/*bool SameSide(Vector3 A, Vector3 B, Vector3 C, Vector3 P)
{
    Vector3 AB = B - A ;
    Vector3 AC = C - A ;
    Vector3 AP = P - A ;

    Vector3 v1 = AB.Cross(AC) ;
    Vector3 v2 = AB.Cross(AP) ;

    // v1 and v2 should point to the same direction
    return v1.Dot(v2) >= 0 ;
}

// Same side method
// Determine whether point P in triangle ABC
bool PointinTriangle1(Vector3 A, Vector3 B, Vector3 C, Vector3 P)
{
    return SameSide(A, B, C, P) &&
        SameSide(B, C, A, P) &&
        SameSide(C, A, B, P) ;
}*/
bool PointinTriangle(Vector3 A, Vector3 B, Vector3 C, Vector3 P){
	// P = A + u (B-A) + v (C-A);
	// u + v <= 1, u >= 0, v >= 0
    Vector3 v0 = C - A ;
    Vector3 v1 = B - A ;
    Vector3 v2 = P - A ;

    float dot00 = v0.Dot(v0) ;
    float dot01 = v0.Dot(v1) ;
    float dot02 = v0.Dot(v2) ;
    float dot11 = v1.Dot(v1) ;
    float dot12 = v1.Dot(v2) ;

    float inverDeno = 1 / (dot00 * dot11 - dot01 * dot01) ;

    float u = (dot11 * dot02 - dot01 * dot12) * inverDeno ;
    if (u < 0 || u > 1) // if u out of range, return directly
        return false ;

    float v = (dot00 * dot12 - dot01 * dot02) * inverDeno ;
    if (v < 0 || v > 1) // if v out of range, return directly
        return false ;

    return u + v <= 1 ;
}

class Flee{
  public:
    double maximalSafetyLevel(vector <int> x, vector <int> y){
		int n = x.size();
		double ans1 = 5000, ans2 = 0, temp;
		for(int i=0; i<n; i++){
			temp = sqrt(x[i]*x[i] + y[i]*y[i]);
			ans1 = min(ans1, temp);
			cout<<temp<<" "<<ans1<<endl;
		}
		if(n<3)
			return ans1;
		Vector3 t[3];
		for(int i=0; i<3; i++)
			t[i] = Vector3(x[i], y[i], 0);
		Vector3 P(0,0,0);
		if(!PointinTriangle(t[0], t[1], t[2], P))
			return ans1;
		for(int i=0; i<n-1; i++)
			for(int j=i+1; j<n; j++){
				temp = sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]))/2.0;
				ans2 = max(ans2, temp);
				cout<<temp<<" "<<ans2<<endl;
			}
		return min(ans1, ans2);
	}
};

int main(){
#ifdef SZY
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int a[] = {232,312,-432};
	int b[] = {498,-374,24};
	vector<int> x(a, a+3);
	vector<int> y(b, b+3);
	Flee flee;
	cout<<flee.maximalSafetyLevel(x, y)<<endl;
	return 0;
}