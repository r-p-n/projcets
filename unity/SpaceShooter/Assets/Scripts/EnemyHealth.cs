using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class EnemyHealth : MonoBehaviour
{
    [SerializeField]
    int points = 10;
    [SerializeField]
    private GameObject explosion;
    private Text tscore;

    private void Start()
    {
        GameObject scoreText = GameObject.Find("Score");
        tscore = scoreText.GetComponent<Text>();
    }


    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Player projectile")
        {
            int iscore = int.Parse(tscore.text) + points;
            tscore.text = iscore.ToString();

            Instantiate(explosion, transform.position, Quaternion.identity);

            Destroy(collision.gameObject);
            Destroy(this.gameObject);
        }
    }
}
