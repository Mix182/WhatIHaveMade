using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Game_tutorial
{
    public partial class Form1 : Form
    {
        Player player;

        int[] winSize = new int[2];

        Map grid;
        List<List<string>> mapy = maps.getMaps();

        int level = 0;

        bool[] movment = new bool[3];

        public Form1()
        {
            InitializeComponent();
            init();
        }

        public void init()
        {
            winSize = getWinSize();
            grid = new Map(mapy[level], winSize);
            player = new Player(grid.player.x, grid.player.y, grid.player.w, grid.player.h, Color.FromArgb(0, 200, 0), grid);
        }

        public int[] getWinSize()
        {
            int[] ws = new int[2];

            ws[0] = this.ClientSize.Width;
            ws[1] = this.ClientSize.Height;

            return ws;
        }
        private void resize(object sender, EventArgs e)
        {
            Invalidate();
            init();
        }
        private void draw(object sender, PaintEventArgs e)
        {
            Graphics win = e.Graphics;

            grid.draw(win);
            player.draw(win);
        }
        private void main(object sender, EventArgs e)
        {
            player.update(movment, grid);
        }
        private void keyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.A || e.KeyCode == Keys.Left)
            {
                this.movment[0] = true;
            }
            else if (e.KeyCode == Keys.W || e.KeyCode == Keys.Space || e.KeyCode == Keys.Up)
            {
                this.movment[1] = true;
            }
            else if (e.KeyCode == Keys.D || e.KeyCode == Keys.Right)
            {
                this.movment[2] = true;
            }
        }
        private void keyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.A || e.KeyCode == Keys.Left)
            {
                this.movment[0] = false;
            }
            else if (e.KeyCode == Keys.W || e.KeyCode == Keys.Space || e.KeyCode == Keys.Up)
            {
                this.movment[1] = false;
            }
            else if (e.KeyCode == Keys.D || e.KeyCode == Keys.Right)
            {
                this.movment[2] = false;
            }
        }
    }
    public class Rect
    {
        public int x = 0;
        public int y = 0;
        public int w = 0;
        public int h = 0;
        public Brush br;
        public string type;
        public Rect(int x, int y, int w, int h, Color col, string type = "none")
        {
            this.x = x;
            this.y = y;
            this.w = w;
            this.h = h;

            this.br = new SolidBrush(col);

            this.type = type;
        }
        public void draw(Graphics win)
        {
            win.FillRectangle(this.br, this.x, this.y, this.w, this.h);
        }
        public bool collision(Rect rect)
        {
            int l1 = this.x;
            int r1 = this.x + this.w;
            int t1 = this.y;
            int b1 = this.y + this.h;

            int l2 = rect.x;
            int r2 = rect.x + rect.w;
            int t2 = rect.y;
            int b2 = rect.y + rect.h;

            if (((l1 < r2) && (r1 > l2)) && (t1 < b2) && (b1 > t2))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
    public class Map
    {
        List<Rect> map = new List<Rect>();

        public int[] ss = new int[2];
        int[] sc = new int[2];
        public int coins;

        public Rect player;

        List<string> saMap;

        public Map(List<string> sMap, int[] vs)
        {
            sc[0] = sMap[0].Length;
            sc[1] = sMap.Count;

            this.saMap = sMap;
            update(vs);
        }
        public bool blockCollision(Rect rect)
        {
            foreach (Rect y in map)
            {
                if (y.type == "block" && y.collision(rect))
                {
                    return true;
                }
            }
            return false;
        }
        public bool coinCollision(Rect rect)
        {
            for (int y = 0; y < map.Count; y++)
            {
                if (map[y].type == "coin" && map[y].collision(rect))
                {
                    coins--;
                    map.RemoveAt(y);
                    return true;
                }
            }
            return false;
        }
        public void draw(Graphics win)
        {
            foreach (Rect y in map)
            {
                y.draw(win);
            }
        }
        public void construct()
        {
            List<string> sMap = this.saMap;
            map = new List<Rect>();

            for (int y = 0; y < sMap.Count; y++)
            {
                for (int x = 0; x < sMap[y].Length; x++)
                {
                    if (sMap[y][x].ToString() == "#")
                    {
                        map.Add(new Rect(x * ss[0], y * ss[1], ss[0], ss[1], Color.FromArgb(100, 100, 100), type: "block"));
                    }
                    else if (sMap[y][x].ToString() == "S")
                    {
                        player = new Rect(Convert.ToInt32(x * ss[0] + ss[0] * 0.1), Convert.ToInt32(y * ss[1] + ss[1] * 0.1), Convert.ToInt32(ss[0] - (ss[0] * 0.2)), Convert.ToInt32(ss[1] - (ss[1] * 0.2)), Color.FromArgb(0, 0, 0));
                    }
                    else if (sMap[y][x].ToString() == "C")
                    {
                        coins++;
                        map.Add(new Rect(Convert.ToInt32(x * ss[0] + ss[0] * 0.2), Convert.ToInt32(y * ss[1] + ss[1] * 0.2), Convert.ToInt32(ss[0] - (ss[0] * 0.4)), Convert.ToInt32(ss[1] - (ss[1] * 0.4)), Color.FromArgb(250, 250, 0), type: "coin"));
                    }
                }
            }
        }
        public void update(int[] vs)
        {
            ss[0] = vs[0] / sc[0];
            ss[1] = vs[1] / sc[1];
            construct();
        }
    }
    public class Player : Rect
    {
        int speed;
        int jump;
        int g;
        int[] maxSpeed = new int[2];
        int[] force = new int[2];
        public Player(int x, int y, int w, int h, Color col, Map grid) : base(x, y, w, h, col) 
        {
            speed = grid.ss[0] / 100;
            jump = grid.ss[1] / 10;
            g = grid.ss[1] / 80;
            maxSpeed[0] = grid.ss[0] / 10;
            maxSpeed[1] = grid.ss[1] / 8;
            force[0] = 0;
            force[1] = 0;
        }
        public void update(bool[] movement, Map grid)
        {
            if (movement[0])
            {
                force[0] -= speed;
                if(force[0] < (maxSpeed[0] * -1))
                {
                    force[0] = (maxSpeed[0] * -1);
                }
            }
            if (movement[2])
            {
                force[0] += speed;
                if (force[0] > maxSpeed[0])
                {
                    force[0] = maxSpeed[0];
                }
            }
            if (movement[1])
            {
                force[1] = jump;
            }
            force[1] -= g;

            int nx;
            int ny;
            int nw;
            int nh;

            if(force[0] > 0)
            {
                nx = this.x;
                nw = this.w + force[0];
                if (grid.blockCollision(new Rect(nx, this.y, nw, this.h, Color.FromArgb(0, 0, 0))))
                {
                    force[0] = 0;
                }
                else
                {
                    this.x += force[0];
                }
            }
            else if (force[0] < 0)
            {
                nx = this.x - force[0];
                nw = this.w + force[0];
                if (grid.blockCollision(new Rect(nx, this.y, nw, this.h, Color.FromArgb(0, 0, 0))))
                {
                    force[0] = 0;
                }
                else
                {
                    this.x += force[0];
                }
            }

            if (force[1] > 0)
            {
                ny = this.y;
                nh = this.h + force[1];
                if (grid.blockCollision(new Rect(this.x, ny, this.w, nh, Color.FromArgb(0, 0, 0))))
                {
                    force[1] = 0;
                }
                else
                {
                    this.x += force[0];
                }
            }
        
            else if (force[1] < 0)
            {
                ny = this.y - force[1];
                nh = this.h + force[1];
                if (grid.blockCollision(new Rect(this.x, ny, this.w, nh, Color.FromArgb(0, 0, 0))))
                {
                    force[1] = 0;
                }
                else
                {
                    this.x += force[0];
                }
            }
        }
    }
    public class maps
    {
        public static List<List<string>> getMaps()
        {
            List<List<string>> map = new List<List<string>> { };
            List<string> map1 = new List<string>
            {
                "##########",
                "# C      #",
                "# #  C   #",
                "#    #   #",
                "# C      #",
                "# #    C #",
                "#   C  # #",
                "#   #    #",
                "#S       #",
                "##########"
            };
            map.Add(map1);
            return map;
        }
    }
}
