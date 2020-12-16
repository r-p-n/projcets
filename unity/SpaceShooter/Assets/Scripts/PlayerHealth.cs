using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class PlayerHealth : MonoBehaviour
{
    [SerializeField]
    private int health = 3;
    [SerializeField]
    private GameObject explosion;
    [SerializeField]
    private GameObject hit;
    private Text t_health;
    private Text gameStatusText; 

    void Start()
    {
        GameObject healthText = GameObject.Find("Health");
        t_health = healthText.GetComponent<Text>();
        t_health.text = health.ToString();

        GameObject gameOverText = GameObject.Find("Game Over Text");
        gameStatusText = gameOverText.GetComponent<Text>();
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "projectile")
        {
            health--;
            t_health.text = health.ToString();
            Instantiate(hit, transform.position, Quaternion.identity);
            Destroy(collision.gameObject);

            if (health <= 0)
            {
                Instantiate(explosion, transform.position, Quaternion.identity);
                GameOver();
            }
        }
    }

    void GameOver()
    {
        Destroy(this.gameObject);
        gameStatusText.text = "GAME OVER";
        SceneManager.LoadScene("game_over");
    }
}
